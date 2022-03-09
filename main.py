import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')

st.write('DataFrame')

'start!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)
    

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

df = pd.DataFrame({
    '1列目' : [1,2,3,4],
    '2列目': [10,20,30,40]
})

st.write(df)
st.dataframe(df.style.highlight_max(axis = 0), width = 500, height = 200)
st.table(df)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a','b','c']
)

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

st.map(df3)

st.write('Display Image')

if st.checkbox('Show Image'):

    img = Image.open('IMG_3402.jpg')
    st.image(img, caption = 'Starbacks', use_column_width = True)

option = st.selectbox(
    'あなたが好きな数字を入れてください',
    list(range(1,11))
)

'あなたの好きな数字は', option, 'です'

st.write('Interactive Widgets')

option2 = st.sidebar.text_input('あなたの趣味を教えてください。')
st.sidebar.write('あなたの趣味は', option2, 'です。')

condition = st.sidebar.slider('あなたの今の調子は?', 0, 100, 50)
st.sidebar.write('コンディション:', condition)

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
















