import pandas as pd
import streamlit as st
from signalUnivariateStudy.SignalUnivariateStudy import SignalUnivariateStudy
import seaborn as sns
sns.set()

@st.cache
def load_data():
    return pd.read_csv("stock_data_actual_dates.csv")

df = load_data()

st.dataframe(df.dropna().head(10))

# df
list_factors = ['momentum', 'quality', 'growth', 'vol', 'value', 'size']

factor = st.selectbox("factor",list_factors)

bt = SignalUnivariateStudy(data_df=df,
                           factor_name=factor,
                           stock_col_name='stock',
                           neutralizer_column='sector',
                           order='asc',
                           n=5)
#bt.stats.columns

bt.stats.index = ['returns', 'volatility', 'sharpe', 'tstat', 'maxDD',
                  'start_dt', 'end_dt', 'freq', 'order', 'n_buckets']

pd.DataFrame(bt.stats)

stats = bt.stats.reset_index()
stats['index'] = stats['index'].astype(object)

st.dataframe(stats)
#
#st.dataframe(stats.style.highlight_max(axis=0))
format_dict = {'1':'{:.2%}'}

stats.style.format(format_dict)

#stats.style.format(formatters = )

#st.dataframe(bt.wealth)

#bt.stats
bt.wealth.plot()

st.pyplot()

