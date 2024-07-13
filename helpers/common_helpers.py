from typing import Union
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import shapiro, kstest, normaltest, norm, kruskal, f_oneway, tukey_hsd
import pprint


def is_data_normal(data: [], method="normaltest") -> bool:
    if method == "normaltest":
        stat, p = normaltest(data)
    elif method == "shapiro":
        stat, p = shapiro(data)
    if p < 0.05:
        return False
    else:
        return True


def is_the_mean_different(*samples, method="one_way_anova") -> bool:
    if method == "one_way_anova":
        stat, p = f_oneway(*samples[0])
    else:
        stat, p = kruskal(*samples[0])
    if p < 0.05:
        return True
    else:
        return False


def generate_standard_plot_and_stats_for_1d_data(data: Union[pd.Series, list], show_plot=True, xlab="",
                                                 ylab="") -> dict:
    if show_plot:
        plt.figure()
        plt.boxplot(data)
        plt.violinplot(data, widths=0.3)
        plt.scatter(np.ones(len(data)), data)
        plt.scatter(np.linspace(0.5, 1.5, len(data)), data)
        plt.xlim(0.2, 1.7)
        plt.ylabel(ylab)
        plt.xlabel(xlab)
        plt.grid()
        # plt.show()
    minimum = min(data)
    maximum = max(data)
    median = np.median(data)
    average = np.average(data)
    q75, q25 = np.percentile(data, [75, 25])
    iqr = q75 - q25
    n = len(data)
    stdev = np.std(data)
    if isinstance(data, pd.Series):
        data = data.to_list()
    norm_test = np.round(normaltest(data).pvalue, 3)
    shap = np.round(shapiro(data).pvalue, 3)
    kolmogorov = np.round(kstest(data, norm.cdf).pvalue, 3)
    loc = locals()
    stats = dict(
        [(i, np.round(loc[i] * 100) / 100) for i in
         ("minimum", "maximum", "median", "average", "q25", "q75", "iqr", "n", "stdev")])
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(stats)
    normality = dict(
        [(i, np.round(loc[i] * 100) / 100) for i in ("shap", "kolmogorov", "norm_test")])
    pp.pprint(normality)
    return stats

def entry_questionnaire_analyzer(df: pd.DataFrame) -> pd.DataFrame:
    eq_df = df[df["stepName"] == "entry-questionnaire"]
    eq_df.reset_index(inplace=True)
    vals = eq_df["stepValue"].to_list()
    new_vals = []
    for index, value in enumerate(vals):
        val = value.replace("$$", "")
        complete_val = val
        complete_val = complete_val.replace('true', '"true"')
        complete_val = complete_val.replace('false', '"false"')
        complete_val = complete_val.replace('""', '"')
        cv = eval(complete_val)
        entry_dict = cv["entryQuestionnaire"]
        cv.pop("entryQuestionnaire")
        new_vals.append({**entry_dict, **cv})
    vals_df = pd.DataFrame(new_vals)
    eq_final = pd.concat([eq_df.loc[:, ["userID", "sessionID"]], vals_df], axis=1)
    return eq_final


def get_user_intersection(*args: pd.DataFrame) -> list:
    common_users = []
    for index, arg in enumerate(args):
        if index == 0:
            common_users = list(arg["userID"].unique())
            continue
        temp_users = list(arg["userID"].unique())
        new_common_users = [user for user in temp_users if user in common_users]
        common_users = new_common_users
    return common_users

def end_questionnaire_analyzer(df: pd.DataFrame) -> pd.DataFrame:
    eq_df = df[df["stepName"] == "end-questionnaire"]
    eq_df.reset_index(inplace=True)
    vals = eq_df["stepValue"].to_list()
    new_vals = []
    for index, value in enumerate(vals):
        val = value.replace("$$", "")
        complete_val = val.replace('true', '"true"')
        complete_val = complete_val.replace('false', '"false"')
        complete_val = complete_val.replace('\\"', '')
        new_vals.append(eval(complete_val))
    vals_df = pd.DataFrame(new_vals)
    eq_final = pd.concat([eq_df.loc[:, ["userID", "sessionID"]], vals_df], axis=1)
    return eq_final


def are_tasks_understood(item: dict, userID: str) -> bool:
    try:
        selected_answer = list(item["checkboxesStatuses"].values()).index('true') + 1
    except ValueError:
        return False
    if item["correctAnswer"] == selected_answer:
        return True
    else:
        return False

def cvd_analyzer(df: pd.DataFrame) -> pd.DataFrame:
    cvd = df[df["stepName"] == "cvd-test"]
    cvd.reset_index(inplace=True)
    vals = cvd["stepValue"].to_list()
    vals_dict = [eval(item.replace("$$", ""))["recordedResults"] for item in vals]
    vals_df = pd.DataFrame(vals_dict)
    cvd_df = pd.concat([cvd.loc[:, ["userID", "sessionID"]], vals_df], axis=1)
    return cvd_df

def common_members_dfs(t0_df_merged, t1_df_merged, t2_df_merged, t3_df_merged, common_users):
    t0_common = t0_df_merged[t0_df_merged["userID"].isin(common_users)]
    t1_common = t1_df_merged[t1_df_merged["userID"].isin(common_users)]
    t2_common = t2_df_merged[t2_df_merged["userID"].isin(common_users)]
    t3_common = t3_df_merged[t3_df_merged["userID"].isin(common_users)]
    return t0_common, t1_common, t2_common, t3_common