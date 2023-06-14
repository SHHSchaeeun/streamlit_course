import streamlit as st
import pandas as pd
import io

df = pd.read_csv('global_internet_users/global_internet_users.csv')

world_df = df[df['Code'].str.contains('OWID_WRL')].copy()
world_df = world_df.drop([world_df.columns[0], world_df.columns[1], world_df.columns[2]], axis='columns')

region_df = df[df['Code'].str.contains('Region')].copy()
region_df = region_df.drop([region_df.columns[0]], axis='columns')

desired_values = ['High income', 'Low and middle income', 'Low income',
                  'Lower middle income', 'Middle income', 'Upper middle income']

income_df = region_df[region_df['Entity'].isin(desired_values)].copy()
region_df = region_df[~region_df['Entity'].isin(desired_values)].copy()

st.title(':globe_with_meridians: Global Internet Users')

mnu = st.sidebar.selectbox('메뉴', options=['설명', 'EDA', '시각화', '모델링'])

if mnu == '설명':
    st.subheader('설명')
    st.markdown('''
    **▍ 인터넷이란?**
    :a 인터넷은 인터넷 프로토콜 스위트(TCP/IP)를 사용하여 네트워크와 장치 간에 통신하는 상호 연결된 컴퓨터 네트워크의 글로벌 시스템입니다. 
    광범위한 전자, 무선 및 광 네트워킹 기술로 연결된 로컬에서 글로벌 범위의 민간, 공공, 학술, 비즈니스 및 정부 네트워크로 구성된 네트워크입니다. 
    인터넷은 연결된 하이퍼텍스트 문서 및 WWW(World Wide Web)의 응용프로그램, 전자 메일, 전화 및 파일 공유와 같은 광범위한 정보 리소스 및 서비스를 제공합니다.
    ''')
    st.image('https://cdn.pixabay.com/photo/2017/07/27/18/12/man-2546224_1280.png')
    st.markdown('''
    **▍ 데이터 세트 소개**
    :a 'Global Internet Users' 데이터 세트에는 1980-2020년 인터넷 사용자에 대한 정보가 있습니다. 
    :a 열에 대한 자세한 내용은 다음과 같습니다:
    * **Entity** - 국가 및 지역의 이름을 포함합니다.
    * **Code** - 국가 코드에 대한 정보이며 코드에 'Region' 값이 있는 경우 여러 국가를 그룹화하여 구분을 나타냅니다.
    * **Year** - 1980년부터 2020년까지의 연도입니다.
    * **Cellular Subscription** - 인구 100명당 휴대폰 구독 수입니다. 
    평균적으로 한 사람이 모바일 서비스를 두 개 이상 구독하는 경우 이 수치는 100을 초과할 수 있습니다.
    * **Internet Users(%)** - 전 세계 모든 국가에서 인터넷에 접속하는 인구의 비율입니다.
    * **No. of Internet Users** - 모든 국가에서 인터넷을 사용하는 인구 수입니다.
    * **Broadband Subscription** - 인구 100명당 고정 광대역 가입 건수입니다. 
    이는 256kbit/s 이상의 다운스트림 속도로 공용 인터넷에 고속 액세스(TCP/IP 연결)하는 고정 구독을 의미합니다.
    ''')
    st.markdown('''
    **▍ 데이터 분석 목표**
    :a 세계의 인터넷 사용자 수가 어떻게 증가하는지 시각화하여 살펴보고, 예측값을 그래프로 나타냅니다.
    ''')
    st.caption('https://www.kaggle.com/datasets/ashishraut64/internet-users')

elif mnu == 'EDA':

    st.subheader('EDA')
    st.markdown('* 기존 데이터 shape')
    st.text(f'{df.shape}')
    st.markdown('* 기존 데이터')
    st.write(df)
    st.markdown('* 세계 데이터')
    st.write(world_df)
    st.markdown('* 지역 데이터')
    st.write(region_df)
    st.markdown('* 소득별 데이터')
    st.write(income_df)

    buffer = io.StringIO()

    st.markdown('* world_df.info :a world_df.dtypes',
                help='참고한 자료에서 world_df.dtypes를 썼는데 데이터 칼럼은 이게 더 깔끔한 것 같아서 함께 사용했습니다.')
    world_df.info(buf=buffer)
    st.text(buffer.getvalue())
    st.write(world_df.dtypes)

    buffer.truncate(0)

    st.markdown('* region_df.info() :a region_df.dtypes')
    region_df.info(buf=buffer)
    st.text(buffer.getvalue())
    st.write(region_df.dtypes)

    buffer.truncate(0)

    st.markdown('* income_df.info() :a income_df.dtypes')
    income_df.info(buf=buffer)
    st.text(buffer.getvalue())
    st.write(income_df.dtypes)

elif mnu == '시각화':
    import seaborn as sns
    import plotly.express as px
    import matplotlib.pyplot as plt

    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.subheader('시각화')

    st.caption('우측 상단 메뉴-Settings에서 Wide mode를 체크하시면 보시기에 좋습니다.')

    st.markdown('* **전세계**')
    col1, col2, col3 = st.columns(3)

    with col1:
        plt.figure(figsize=(6, 6))
        sns.lineplot(x='Year', y='Internet Users(%)', data=world_df)
        st.markdown('인터넷 사용자 수')
        st.pyplot()

    with col2:
        plt.figure(figsize=(6, 6))
        sns.lineplot(x='Year', y='Cellular Subscription', data=world_df)
        st.markdown('휴대폰 구독 건수')
        st.pyplot()

    with col3:
        plt.figure(figsize=(6, 6))
        sns.lineplot(x='Year', y='Broadband Subscription', data=world_df)
        st.markdown('고정 광대역 가입 건수')
        st.pyplot()

    st.markdown('* **지역별**')
    col1, col2, col3 = st.columns(3)

    with col1:
        plt.figure(figsize=(6, 6))
        sns.lineplot(x='Year', y='Internet Users(%)', hue='Entity', data=region_df)
        st.markdown('인터넷 사용자 수')
        st.pyplot()

    with col2:
        plt.figure(figsize=(6, 6))
        sns.lineplot(x='Year', y='Cellular Subscription', hue='Entity', data=region_df)
        st.markdown('휴대폰 구독 건수')
        st.pyplot()

    with col3:
        plt.figure(figsize=(6, 6))
        sns.lineplot(x='Year', y='Broadband Subscription', hue='Entity', data=region_df)
        st.markdown('고정 광대역 가입 건수')
        st.pyplot()

    st.markdown('* **소득별**')
    col1, col2, col3 = st.columns(3)

    with col1:
        plt.figure(figsize=(6, 6))
        sns.lineplot(x='Year', y='Internet Users(%)', hue='Entity', data=income_df)
        st.markdown('인터넷 사용자 수')
        st.pyplot()

    with col2:
        plt.figure(figsize=(6, 6))
        sns.lineplot(x='Year', y='Cellular Subscription', hue='Entity', data=income_df)
        st.markdown('휴대폰 구독 건수')
        st.pyplot()

    with col3:
        plt.figure(figsize=(6, 6))
        sns.lineplot(x='Year', y='Broadband Subscription', hue='Entity', data=income_df)
        st.markdown('고정 광대역 가입 건수')
        st.pyplot()

    st.markdown('* 인터넷 사용자(2020) 지역별 시각화')
    df_2020 = df[df['Year'] == 2020]
    fig = px.choropleth(df_2020,
                        locations='Code',
                        color='No. of Internet Users',
                        hover_name='Entity',
                        color_continuous_scale='RdBu',
                        range_color=(0, 200000000),
                        )

    fig.update_layout(
        title_text='Number of Internet Users in 2020',
        coloraxis_colorbar=dict(
            title='No. of Internet Users',
            dtick=20000000,
            tickformat='.0s',
        )
    )
    st.write(fig)

elif mnu == '모델링':
    import seaborn as sns
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    st.set_option('deprecation.showPyplotGlobalUse', False)

    from statsmodels.tsa.seasonal import seasonal_decompose
    from statsmodels.tsa.statespace.sarimax import SARIMAX
    from pandas.tseries.offsets import DateOffset

    st.subheader('모델링')

    st.markdown('''
    * **사용한 모델링**
    :a **SARIMAX** (Seasonal Auto-Regressive Integrated Moving Average with eXogenous factors)는 ARIMA 모델을 일반화한 것으로, 
    :a 시계열 데이터의 패턴을 학습하고 예측하는데 사용됩니다. 
    :a S는 계절성을 포함, 외생변수 X를 포함한다는 것을 의미합니다.
    ''', help='외생변수란 모형 밖에서 결정되는 값으로, 밖에서 값이 주어지고 모형에 영향을 주는 변수입니다.')

    st.markdown('* 데이터를 다시 불러옵니다(오류 방지)')
    df = pd.read_csv('global_internet_users/global_internet_users.csv')
    world_df = df[df['Code'].str.contains('OWID_WRL')].copy()
    world_df = world_df[~world_df['Year'].between(1980, 1989)]
    world_df.reset_index(drop=True, inplace=True)
    world_df['Year'] = pd.to_datetime(world_df['Year'], format='%Y')
    st.write(world_df)
    buffer = io.StringIO()
    st.markdown('* world_df.info :a world_df.dtypes')
    world_df.info(buf=buffer)
    st.text(buffer.getvalue())
    st.write(world_df.dtypes)

    st.markdown('* Internet Users(%) over Time')
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=world_df, x='Year', y='Internet Users(%)')
    plt.xlabel('Year')
    plt.ylabel('Internet Users(%)')
    st.pyplot()

    st.markdown('* 데이터를 연간으로 쪼개고, '
                ':a trend, seasonal, residual(잔차)를 시각화합니다.')
    world_df.set_index('Year', inplace=True)
    world_df.index = pd.PeriodIndex(world_df.index, freq='A-DEC')  # Convert the index to a PeriodIndex with yearly frequency
    world_df.index = world_df.index.to_timestamp()  # Convert the index to datetime format for plotting
    decomposition = seasonal_decompose(world_df['Internet Users(%)'], period=1)  # Decompose the time series
    decomposition.plot()
    st.pyplot()

    st.markdown('* SARIMAX model을 통해 향후 5년간의 증가율을 예측합니다.')

    st.code('''
    # Fit a SARIMAX model
    model = SARIMAX(world_df['Internet Users(%)'], order=(1, 1, 1))
    results = model.fit(disp=-1)

    # Generate forecast for the next 5 years
    future_years = [world_df.index[-1] + DateOffset(years=x) for x in range(1, 6)]
    future_years_df = pd.DataFrame(index=future_years, columns=world_df.columns)
    future_df = pd.concat([world_df, future_years_df])

    # Predict for the next 5 years
    future_df['forecast'] = results.predict(start=len(world_df), end=len(world_df) + 5, dynamic=True)

    # Plot the original data, the fitted values, and the forecast
    plt.figure(figsize=(12, 6))
    plt.plot(future_df['Internet Users(%)'], label='Original')
    plt.plot(future_df['forecast'], label='Forecast')
    plt.legend(loc='best')
    st.pyplot()
    ''')

    # Fit a SARIMAX model
    model = SARIMAX(world_df['Internet Users(%)'], order=(1, 1, 1))
    results = model.fit(disp=-1)

    # Generate forecast for the next 5 years
    future_years = [world_df.index[-1] + DateOffset(years=x) for x in range(1, 6)]
    future_years_df = pd.DataFrame(index=future_years, columns=world_df.columns)
    future_df = pd.concat([world_df, future_years_df])

    # Predict for the next 5 years
    future_df['forecast'] = results.predict(start=len(world_df), end=len(world_df) + 5, dynamic=True)

    # Plot the original data, the fitted values, and the forecast
    plt.figure(figsize=(12, 6))
    plt.plot(future_df['Internet Users(%)'], label='Original')
    plt.plot(future_df['forecast'], label='Forecast')
    plt.legend(loc='best')
    st.pyplot()
