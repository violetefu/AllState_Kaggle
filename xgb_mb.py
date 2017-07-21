import numpy as np
import pandas as pd
import xgboost as xgb
from datetime import datetime
from sklearn.metrics import mean_absolute_error
from sklearn.cross_validation import KFold
from scipy.stats import skew, boxcox
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import itertools

shift = 200
COMB_FEATURE = 'cat80,cat87,cat57,cat12,cat79,cat10,cat7,cat89,cat2,cat72,' \
               'cat81,cat11,cat1,cat13,cat9,cat3,cat16,cat90,cat23,cat36,' \
               'cat73,cat103,cat40,cat28,cat111,cat6,cat76,cat50,cat5,' \
               'cat4,cat14,cat38,cat24,cat82,cat25'.split(',')

def encode(charcode):
    r = 0
    ln = len(str(charcode))
    for i in range(ln):
        r += (ord(str(charcode)[i]) - ord('A') + 1) * 26 ** (ln - i - 1)
    return r

def log_mae(labels,preds, lift=200):
    return mean_absolute_error(np.exp(labels)-lift, np.exp(preds)-lift)

fair_constant = 0.7
def fair_obj(preds, dtrain):
    labels = dtrain.get_label()
    x = (preds - labels)
    den = abs(x) + fair_constant
    grad = fair_constant * x / (den)
    hess = fair_constant * fair_constant / (den * den)
    return grad, hess

def xg_eval_mae(yhat, dtrain):
    y = dtrain.get_label()
    return 'mae', mean_absolute_error(np.exp(y)-shift,
                                      np.exp(yhat)-shift)
def mungeskewed(train, test, numeric_feats):
    ntrain = train.shape[0]
    test['loss'] = 0
    train_test = pd.concat((train, test)).reset_index(drop=True)
    skewed_feats = train[numeric_feats].apply(lambda x: skew(x.dropna()))
    skewed_feats = skewed_feats[skewed_feats > 0.25]

    skewed_feats = skewed_feats.index
    for feats in skewed_feats:
        train_test[feats] = train_test[feats] + 1
        train_test[feats], lam = boxcox(train_test[feats])
    return train_test, ntrain

if __name__ == "__main__":
    print('\nStarted')
    train = pd.read_csv('../input/train.csv')
    test = pd.read_csv('../input/test.csv')

    numeric_feats = [x for x in train.columns[1:-1] if 'cont' in x]
    categorical_feats = [x for x in train.columns[1:-1] if 'cat' in x]
    train_test, ntrain = mungeskewed(train, test, numeric_feats)
    
    # taken from Vladimir's script (https://www.kaggle.com/iglovikov/allstate-claims-severity/xgb-1114)
    for column in list(train.select_dtypes(include=['object']).columns):
        if train[column].nunique() != test[column].nunique():
            set_train = set(train[column].unique())
            set_test = set(test[column].unique())
            remove_train = set_train - set_test
            remove_test = set_test - set_train
            remove = remove_train.union(remove_test)

            def filter_cat(x):
                if x in remove:
                    return np.nan
                return x

            train_test[column] = train_test[column].apply(lambda x: filter_cat(x), 1)

    # taken from Ali's script (https://www.kaggle.com/aliajouz/allstate-claims-severity/singel-model-lb-1117)
    train_test["cont1"] = np.sqrt(preprocessing.minmax_scale(train_test["cont1"]))
    train_test["cont4"] = np.sqrt(preprocessing.minmax_scale(train_test["cont4"]))
    train_test["cont5"] = np.sqrt(preprocessing.minmax_scale(train_test["cont5"]))
    train_test["cont8"] = np.sqrt(preprocessing.minmax_scale(train_test["cont8"]))
    train_test["cont10"] = np.sqrt(preprocessing.minmax_scale(train_test["cont10"]))
    train_test["cont11"] = np.sqrt(preprocessing.minmax_scale(train_test["cont11"]))
    train_test["cont12"] = np.sqrt(preprocessing.minmax_scale(train_test["cont12"]))
    train_test["cont6"] = np.log(preprocessing.minmax_scale(train_test["cont6"]) + 0000.1)
    train_test["cont7"] = np.log(preprocessing.minmax_scale(train_test["cont7"]) + 0000.1)
    train_test["cont9"] = np.log(preprocessing.minmax_scale(train_test["cont9"]) + 0000.1)
    train_test["cont13"] = np.log(preprocessing.minmax_scale(train_test["cont13"]) + 0000.1)
    train_test["cont14"] = (np.maximum(train_test["cont14"] - 0.179722, 0) / 0.665122) ** 0.25

    for comb in itertools.combinations(COMB_FEATURE, 2):
        feat = comb[0] + "_" + comb[1]
        train_test[feat] = train_test[comb[0]] + train_test[comb[1]]
        train_test[feat] = train_test[feat].apply(encode)

    for col in categorical_feats:
        print('Analyzing Column:', col)
        train_test[col] = train_test[col].apply(encode)

    ss = StandardScaler()
    train_test[numeric_feats] = \
        ss.fit_transform(train_test[numeric_feats].values)

    train = train_test.iloc[:ntrain, :].copy()
    test = train_test.iloc[ntrain:, :].copy()

    print('\nMedian Loss:', train.loss.median())
    print('Mean Loss:', train.loss.mean())

    ids = pd.read_csv('../input/test.csv')['id']
    train_y = np.log(train.loss.values + shift)
    train_x = train.drop(['loss','id'], axis=1).values
    test_x = test.drop(['loss','id'], axis=1).values
    del train_test, train, test

    n_folds = 10

    best_rounds = []
    scores=[]

    train_pred = np.zeros((train_x.shape[0], 1))
    test_pred = np.zeros((test_x.shape[0], n_folds))

    kf = KFold(train.shape[0], n_folds=n_folds)
    for i, (train, val) in enumerate(kf):
        est = xgb.XGBRegressor(
                       learning_rate = 0.01,
                       seed = 0,
                       n_estimators = 500000,
                       max_depth= 12,
                       min_child_weight=100, 
                       colsample_bytree=0.7,
                       subsample=0.7,
                       gamma =0.5,
                       objective = 'reg:linear',
                       nthread = -1,
                       silent = True
                      )

        est.fit(train_x[train],train_y[train],
            eval_set=[(train_x[val], train_y[val])], 
            eval_metric = xg_eval_mae, 
            early_stopping_rounds = 200, verbose = False)
        val_y_predict_fold = est.predict(train_x[val])
        train_pred[val,0] = val_y_predict_fold
        test_pred[:,i] = est.predict(test_x)
        score = log_mae(train_y[val], val_y_predict_fold)

        print (score, est.best_iteration)
        scores.append(score)
        best_rounds.append(est.best_iteration)
    print (-np.mean(scores), np.mean(best_rounds))

    train_pred = np.exp(train_pred) - lift
    test_pred = np.exp(test_pred) - lift

    pd.DataFrame(train_pred, columns = ['Pred']).to_csv('../output/train_XGB_mb.csv', index = False)
    test_pred = pd.DataFrame(test_pred, columns = ['Pred_0','Pred_1', 'Pred_2', 'Pred_3', 'Pred_4','Pred_5','Pred_6','Pred_7','Pred_8','Pred_9'])
    test_pred['avgPred'] = test_pred.mean(axis = 1)
    test_pred.to_csv('../output/test_XGB_mb.csv', index = False)
    pd.DataFrame({'id': ids, 'loss': test_pred['avgPred']}).to_csv('../output/submission_XGB_mb.csv', index = False)

