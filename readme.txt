Rep5 -> CV4
8. XGB_Comb101+20_OHE: 1107.83620->1109.41721, n_estimators=20744, obj=logregobj, learning_rate = 0.005, max_depth = 7, min_child_weight = 183, colsample_bytree = 0.2, subsample = 0.8, gamma = 0.5, CV = 1128.35

7. LGB_Comb101+5_OHE_v2: 1109.42594->1109.69728, learning_rate = 0.005, num_iterations=13091, metric='l1', max_bin=430, num_leaves=55, min_data_in_leaf=188, feature_fraction=0.1, bagging_fraction=0.95, CV = 1130.2974926484069
[cont14]+[cat100, cat112, cat113, cat110, cat116]; 101 cat (least importance) combs

13. LGB_CombC+20Aft_LEC1: 1109.86078 (learning_rate=0.005, n_estimators=8371, num_leaves=70, min_child_weight = 230, colsample_bytree = 0.3, subsample = 0.9, subsample_freq = 1, max_bin = 255, reg_alpha = 0.003, CV = 1127.3373103121453)

6. LGB_Comb101+5_OHE_v1: 1109.67249->1110.53253, learning_rate=0.005, num_iterations=20115, metric='l1', max_bin=484, num_leaves=31, min_data_in_leaf=180, feature_fraction=0.1, bagging_fraction=0.8, CV = 1130.8221190362133

11.XGB_Comb101+20_LE_fairobj: ->1110.89367 (n_estimators=19215, obj=fariobj, learning_rate = 0.005, max_depth = 6, min_child_weight = 190, colsample_bytree = 0.8, subsample = 1, gamma = 0.2, CV = 1138.383)

3. LGB_ContNoScale_OHE: 1110.78868->1111.13920, num_iterations=6610, metric='l1', max_bin=483, num_leaves=121, min_data_in_leaf=107, feature_fraction=0.195979, bagging_fraction=0.918178, learning_rate=0.005, CV = 1130.6052460673211

13. LGB_Comb101+20Aft_LE: ->1111.44509 (n_estimators=45509, num_leaves=10, min_child_weightf=179, max_bin=1060, colsample_bytree=0.137, reg_alpha=0.00465 score=1136.88)

2. XGB_CatComb38_OHE: 1111.46004->1112.23090 (n_estimators=38706, obj=logregobj, learning_rate = 0.005, max_depth = 5, min_child_weight = 80, colsample_bytree = 0.1, subsample = 0.7, gamma = 0, CV = 1131.446839)

9. [LGB_Comb101+20_OHE]: ->1112.87792, learning_rate=0.005, num_iterations=37470, metric='l1', max_bin=1140, num_leaves=15, min_data_in_leaf=240, feature_fraction=0.1, bagging_fraction=0.8, CV = 1131.5795

1. xgb_starter: 1111.68603->1113.30717 (CV: -1135.719)

12. LGB_Comb101+20Aft_LE_fairobj: ->1113.95720 (n_estimators=64390, num_leaves=6, min_child_weightf=198, max_bin=433, colsample_bytree=0.248, reg_alpha=0.081963, score=1132.7385)

4. keras_basic10: 1114.18662 (CV4: 0:1149.816542; 1: 1146.888934; 2: 1147.001795; 3: 1147.182164; 4: 1150.962717; 5: 1144.634397; 6: 1149.765304; 7: 1145.837790; 8: 1146.702339; 9: 1144.582434 (*))

[keras_mean_ContNoScale_OHE: 1116.23414]
[keras_starter_ContNoScale_OHE: 1117.56655]

5. keras_mt: 1116.36436, CV4: 1142.362

14. LGB_CombC+20Aft_LE: 1113.73886 (learning_rate=0.005, n_estimators=49428, objective=logregobj, num_leaves=6, min_child_weight = 160, colsample_bytree = 0.8, subsample = 1, subsample_freq = 0, max_bin = 506, reg_alpha = 0.0002, CV = 1133.2285826161731)

15. LGB_CombC+20Aft_LEC2: (learning_rate=0.005, n_estimators=8588, num_leaves=70, min_child_weight = 230, colsample_bytree = 0.25, subsample = 0.9, subsample_freq = 1, max_bin = 255, reg_alpha = 0.003, CV = 1127.3373103121453)

14. LGB_CombC+20Aft_LE2: 1113.73886 (learning_rate=0.005, n_estimators=49428, objective=logregobj, num_leaves=63, min_child_weight = 240, colsample_bytree = 0.2, subsample = 1, subsample_freq = 0, max_bin = 350, reg_alpha = 0.01, CV = 1133.2285826161731)

17. LGB_Comb101+5_OHE_v3: learning_rate=0.005, n_estimators=, objective=logregobj, num_leaves=42, min_child_weight = 160, colsample_bytree = 0.055, subsample = 0.76, subsample_freq = 1, max_bin = 424, reg_alpha = 0.008, CV = 1126.455

Ensemble:
1. (2, 3): 1109.13565
2. (2, 3, 5): 1107.11687
3. (1, 2, 3, 5): 1106.76629
4. (1, 2, 3, 4, 5): 1106.12842 
5. (1, 2, 3, 4, 5, 6): 1105.68182
6. 0.1*(1)+0.15*(2+3+4+5)+0.3*(6): 1105.65567
7. 0.1*(1+2+3+4+5)+0.5*(6): 1105.89597
8. 0.1*(1+4+5)+0.2*(2+3)+0.3*(6): 1105.91792
9. (6, 7): 1109.25488
10. 0.08*(1)+0.12*(2+3+4+5)+0.22*(6+7): 1105.81054
11. 0.1*(1)+0.15*(2+3+4+5+6+7): 1105.69653
12. 0.1*(1)+0.13*(2+3+4+5)+0.19*(6+7): 

13. Ridge_alpha0_avgPred, (1, 2, 3, 6, 7): 1108.01711 (CV=1127.757) => 0.8x + 0.1*(4+5): 1106.2467
14. Ridge_alpha0_logMean, (1, 2, 3, 6, 7): 1108.07433 (CV=1127.757)
15. Ridge_alpha0_allavgPred, (1, 2, 3, 6, 7): 1107.40038 (CV=1127.757) => 0.7x + 0.15*(4+5): 1105.50789 (*)
16. GBlinear_alpha0_allavgPred, (1, 2, 3, 6, 7): 1107.34649 (CV=1127.25)
17. Ridge_alpha0, (1, 2, 3, 6, 7, 8, keras_fu4): 1107.40038 (CV=1125.144)
18. GBlinear_alpha0, (1, 2, 3, 6, 7, 8, keras_fu4): 1105.62059 (CV=1125.01)
19. GBlinear_Ridge, (1, 2, 3, 6, 7, 8, keras_fu4): 1105.57118

20. Ridge_alpha0, (1, 2, 3, 6, 7, 8, keras_fu4):  1105.66851 (CV4=1125.01)
21. GBlinear_alpha0, (1, 2, 3, 6, 7, 8, keras_fu4): 1105.58176 (CV4=1124.99273085) => 1106.17232 (iso) 
22. GBlinear_Ridge, (1, 2, 3, 6, 7, 8, keras_fu4): 1105.53825

23. Ridge_alpha0_cv, (1, 2, 3, 6, 7, 8, 9, 10) 1106.22294, (CV4=1125.142) 
24. Ridge_alpha0_cv, (1, 2, 3, 6, 7, 8, 10) 1105.68830, (CV4=1125.105)
25. Ridge_alpha0_cv10, (1, 2, 3, 6, 7, 8, 10inds) 1105.28320 (CV4=1124.933)
26. Ridge_alpha0_cv10, (all; cv/all) 1105.10361 (CV4=1124.952) (*)
27. Ridge_alpha0_cv10, (all; cv+all) 1105.31990 (CV4=1124.952)

28. Ridge_alpha20_cv10, 1105.66690 (cv), 1105.43789 (all), 1105.51128 (0.5cv+0.5all) (CV4=1124.157)
29. Ridge_alpha0_cv10, 1105.80375 (all-keras_mean), (CV10=1124.326)
29. Ridge_alpha0_cv10, 1105.80375 (all-keras_inds), (CV10=1124.326)
31. Ridge_alpha40_cv10, 1106.29387 (3,7,8,4mean,13), (CV10=1124.483)

32. MCMC10K (sub1-sub15, Keras_avg), 1104.51011; train=1122.5xxx
33. MCMC10Ks (sub1-sub15, Keras_inds), test1-1104.35979; train=1122.6xxx
34. Ridge_alpha15(sub1-sub15, Keras_inds), test1-1105.29618 (CV10=1122.973), Ridge must log_mae
35. mean[33,34] / Ridge_alpha15 + MCMC10Ks: 1104.39123
36. MCMC20K2 (sub1-sub15, Keras_inds, sub3/sub5/sub16 updated), test1-1103.28373; train=1121.5xxx
37. Ridge_alpha0=>MCMC20K2  (sub1-sub15, Keras_inds, sub3/sub5/sub16 updated: 1103.38029; train=1122.253
38. MCMC20K2 (sub1-sub15, Keras_inds, sub3/sub5/sub16 added), test1-1103.20809; train=1121.6xxx
39. MCMC20K3 (sub1-sub16, Keras_inds, sub3/sub5/sub6/sub16 added), test1-1103.61513; train=1121.8xxx
40. MCMC30K (sub1-sub19, Keras_inds, sub3/sub5/sub6/sub16 added), test1-1103.12182; train=1120.6xxx (*)
41. MCMC30K (sub1-sub21, Keras_inds, sub3/sub5/sub6/sub16/sub17/sub18 added), test1-1102.98797; train=1120.4xxx (*)

0: 1120.4992708115944
1: 1120.82
3: 1120.61
9: 1120.8562655693916
10: 
11: 1120.5551318026962
12: 1120.7973365593989
13: 1120.7328
14: 1120.6520
15: 1120.808
16: 1120.877
17: 1120.829
18: 1120.818
19: 1120.682 (0.3) 
20: 1120.613
21: 
22:
23:

24:
25:




=======================
	Basic	Comb38	Comb101+5	Comb101+20	CombC+20
OHE	x,l	x	l	        x, (l)
LE				        x, (l2)	        l

sub6: XGB_Comb101+20_OHE (LB: 1109.41721, CV: 1128.35=>1126.7464)
sub15: LGB_CombC+20Aft_LEC2 (LB: 1109.53902, CV: 1127.3686)
sub5: LGB_Comb101+5_OHE_v2 (LB: 1109.69728, CV: 1130.297=>1126.0060)
sub13: LGB_CombC+20Aft_LEC1 (LB: 1109.86078, CV: 1127.337)
[sub4]: LGB_Comb101+5_OHE_v1 (LB: 1110.53253, CV: 1130.822)
sub11: XGB_Comb101+20_LE_fairobj (LB: 1110.89367, CV: 1138.383)
sub3: LGB_ContNoScale_OHE (LB: 1111.13920,  CV: 1130.6052=>1128.0288)

[=sub12]: LGB_Comb101+20Aft_LE (LB: 1111.44509, CV: 1136.88)
sub2: XGB_CatComb38_OHE (LB: 1112.23090, CV: 1131.447)
[=sub8]: LGB_Comb101+20_OHE (LB: 1112.87792, CV: 1131.5795)
sub1: XGB_starter (LB: 1113.30717, CV: 1135.719)
[(=)sub14]: LGB_CombC+20Aft_LE (LB: 1113.73886, CV: 1133.2286)
[(=)sub10]: LGB_Comb101+20Aft_LE_fairobj (LB: 1113.95720, CV: 1132.7385)
sub7: Keras_Basic (LB: 1114.18662, CV: 1145)
sub9: Keras_MT (LB: 1116.36436, CV: 1142.362)

sub16: LGB_CombC+20Aft_LE2 (LB: , CV: 1124.2766) 

Ridge_alpha0_[sub3, sub5, sub6, sub7sub, sub8, sub12]: 1105.46171 (CV=1124.0339)
Ridge_alpha0_[sub1 - sub12]: 1105.36675 (CV=1124.17928, not the best, CV_alpha10=1124.176)
Ridge_alpha10_[sub1 - sub12]: 1105.80375 (CV10=1124.176)

[sub1, sub2, sub3, sub5, sub6, sub7, sub9, sub11, sub13]: 1105.75983 (alpha0), CV=1123.062, alpha=70; CV=1123.16039, alpha=0;

[sub1-sub14]: 1105.51244 (alpha15), 1105.52357 (alpha0), CV=1122.959, alpha=15; CV=1122.963, alpha=0;

M12: alpha10, 1124.176
-sub1: 1124.172 (10)
-sub2: 1124.117 (1)
-sub4: 1124.135 (3)
-sub9: 1124.166 (10)
-sub10: 1124.160 (0)
-sub11: 1124.169 (3)
-sub7_6: 1124.171 (10)
-sub7_9: 1124.151 (10)
-sub7_6-sub7_9+sub7_avgPred: 1124.153 (10)

del: sub1, sub2, sub4, sub9, sub10, sub11, sub7_6, sub7_9, sub7_avgPred

[sub3, sub5, sub6, sub7sub, sub8, sub12]: 1124.034 (0)


cont14, interaction, group by (2nd, feature)(cont14_mean)

cont12 337 unique values. Slighly curving, 5 year data
cont11 337 unique values. Curving upwards towards the end (predicting higher loss); Something with period of 5. Years? Insurance plan? Slightly distorted to mask the pattern.

cont13 361 values, "period" pattern?
[money]cont7 gap  (which implies that cont6 and cont7 probably measure the same thing); Perhaps premiums paid. Remember cont7 was correlated with Per Capita Income per state; a beta distribution

cont4 Total of 113 unique values, a bit noisy toward the higher end
cont8 unique values 203. There’s also some break at around 0.85


cont14 noisy and irregular. 21372 unique values in total, "period" pattern? money?


Correlated pairs, like 2-3, 4-8 and, possibly, 10-13 are related ordinals binned using different bin sizes. Like cont3 bins size is twice as small as cont2 bin size (or thereabouts). Further I will dare to say that cont2 and cont3 are ages of beneficiary and insurer.[current age, license age]

Cont 6, 7 and 14 are amounts (measure of value?). One of them is related to premiums paid. Some ordinals are related to measures of value

cont5 144 unique values here. Quite ok in the beginning, quite crammed in the higher quarter of the data.

cont14 & cont7 were important features

we do have 2 years worth of data, then that could be a good starting point to talk about life of a product-type analysis and whether the customer mix or profitability changed over time.

Autocorrelation and Partial Autocorrelation (ACF, partial ACF)
Owen's LOO


cat112: 50+DC states of USA 


AddFeature(allSampels, "cont2*cont7"); //cont2*cont7:43.95
AddFeature(allSampels, "cont2+cont7"); //cont2+cont7:30.29
AddFeature(allSampels, "cont1-cont7"); //cont1-cont7:28.91
AddFeature(allSampels, "cont3+cont7"); //cont3+cont7:28.76
AddFeature(allSampels, "cont2*cont12"); //cont2*cont12:26.62
AddFeature(allSampels, "cont2*cont14"); //cont2*cont14:25.23
AddFeature(allSampels, "cont2+cont12"); //cont2+cont12:23.79
AddFeature(allSampels, "cont1+cont13"); //cont1+cont13:23.35
AddFeature(allSampels, "cont2*cont11"); //cont2*cont11:22.51
AddFeature(allSampels, "cont2+cont14"); //cont2+cont14:21.62
AddFeature(allSampels, "cont2*cont8"); //cont2*cont8:21.60
AddFeature(allSampels, "cont3*cont7"); //cont3*cont7:18.06
AddFeature(allSampels, "cont1/cont7"); //cont1/cont7:17.98
AddFeature(allSampels, "cont12-cont13"); //cont12-cont13:17.95
AddFeature(allSampels, "cont2+cont11"); //cont2+cont11:17.53
AddFeature(allSampels, "cont11-cont13"); //cont11-cont13:17.44
AddFeature(allSampels, "cont1-cont9"); //cont1-cont9:17.39
AddFeature(allSampels, "cont4/cont8"); //cont4/cont8:16.61
AddFeature(allSampels, "cont2/cont14"); //cont2/cont14:16.49
AddFeature(allSampels, "cont2-cont14"); //cont2-cont14:15.98
AddFeature(allSampels, "cont13*cont14"); //cont13*cont14:15.85
