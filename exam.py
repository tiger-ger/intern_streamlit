import streamlit as st
import numpy as np
import pandas as pd
import sklearn

st.title('特定のfileでないと実行できません')

train_x_file = st.file_uploader("説明変数X", type='csv')
train_y_file = st.file_uploader("目的変数Y", type='csv')
test_x_file = st.file_uploader("テスト変数X", type='csv')
'二つ同じファイルがないとエラーを吐いてしまったためこのような処理を行っています、このエラーを治すために10時間以上費やしてしまいました。'
test_x_file2 = st.file_uploader("テスト変数Xをもう一度入れてください", type='csv')



if st.button('fileをupload後クリックしてください'):
    train_x = pd.read_csv(train_x_file)
    x = train_x.drop(['職場の様子','（紹介予定）入社後の雇用形態','勤務地　最寄駅3（駅名）','勤務地固定','休日休暇(月曜日)','応募先　名称','（派遣先）配属先部署　男女比　男','勤務地　最寄駅3（沿線名）','（派遣先）勤務先写真コメント','勤務地　最寄駅3（分）','無期雇用派遣','勤務地　最寄駅2（駅名）','未使用.14','（派遣以外）応募後の流れ','（派遣先）概要　従業員数','電話応対なし','（紹介予定）雇用形態備考','週払い','週1日からOK','（派遣先）配属先部署　人数','固定残業制 残業代 下限','残業月20時間以上','職種コード','1日7時間以下勤務OK','ミドル（40〜）活躍中','ルーティンワークがメイン','未使用.11','短時間勤務OK(1日4h以内)','フリー項目　内容','先輩からのメッセージ','対象者設定　年齢下限','未使用.10','土日祝のみ勤務','掲載期間　開始日','動画コメント','Wordのスキルを活かす','未使用.8','経験必須','固定残業制 残業代に充当する労働時間数 下限','給与/交通費　給与支払区分','ブロックコード2','未使用.4','CAD関連のスキルを活かす','未使用.7','お仕事No.','メモ','派遣スタッフ活躍中','ブロックコード3','WEB面接OK','公開区分','17時以降出社OK','寮・社宅あり','20代活躍中','Accessのスキルを活かす','検索対象エリア','就業形態区分','ネットワーク関連のスキルを活かす','Wワーク・副業可能','勤務地　最寄駅2（沿線名）','休日休暇(火曜日)','固定残業制 残業代に充当する労働時間数 上限','プログラム関連のスキルを活かす','未使用.15','平日休みあり','（派遣先）概要　勤務先名（漢字）','勤務地　最寄駅2（駅からの交通手段）','休日休暇　備考','30代活躍中','フラグオプション選択','未使用.12','エルダー（50〜）活躍中','（派遣）応募後の流れ','期間・時間　勤務時間','期間・時間　勤務期間','人材紹介','週2・3日OK','主婦(ママ)・主夫歓迎','勤務先公開','Excelのスキルを活かす','16時前退社OK','正社員登用あり','残業月20時間未満','勤務地　備考','拠点番号','雇用形態','Dip JobsリスティングS','ブロックコード1','フリー項目　タイトル','（紹介予定）入社時期','お仕事名','資格取得支援制度あり','未使用.1','ブランクOK','対象者設定　年齢上限','未使用.20','10時以降出社OK','募集形態','期間・時間　勤務開始日','英語以外の語学力を活かす','勤務地　最寄駅3（駅からの交通手段）','外資系企業','（派遣先）勤務先写真ファイル名','応募先　最寄駅（沿線名）','仕事写真（下）　写真1　ファイル名','PowerPointのスキルを活かす','未使用.16','仕事写真（下）　写真3　ファイル名','オープニングスタッフ','応募先　所在地　ブロックコード','（派遣先）配属先部署','（派遣先）配属先部署　男女比　女','応募先　所在地　都道府県','動画タイトル','仕事内容','（派遣先）概要　事業内容','応募先　最寄駅（駅名）','残業月10時間未満','休日休暇(土曜日)','（紹介予定）年収・給与例','外国人活躍中・留学生歓迎','履歴書不要','未使用.17','休日休暇(木曜日)','未使用.9','日払い','未使用','勤務地　最寄駅1（沿線名）','未使用.18','未使用.22','未使用.5','（派遣先）配属先部署　平均年齢','英語力を活かす','勤務地　周辺情報','仕事写真（下）　写真2　ファイル名','バイク・自転車通勤OK','仕事写真（下）　写真2　コメント','DTP関連のスキルを活かす','会社概要　業界コード','未使用.3','PCスキル不要','車通勤OK','制服あり','給与/交通費　給与上限','休日休暇(水曜日)','未使用.2','WEB関連のスキルを活かす','仕事の仕方','未使用.6','給与　経験者給与下限','勤務地　最寄駅1（駅からの交通手段）','応募資格','学生歓迎','紹介予定派遣','固定残業制 残業代 上限','未使用.19','（紹介予定）休日休暇','給与　経験者給与上限','シフト勤務','経験者優遇','週4日勤務','派遣会社のうれしい特典','土日祝休み','給与/交通費　交通費','掲載期間　終了日','未使用.21','待遇・福利厚生','シニア（60〜）歓迎','ベンチャー企業','少人数の職場','仕事写真（下）　写真3　コメント','新卒・第二新卒歓迎','休日休暇(金曜日)','お仕事のポイント（仕事PR）','産休育休取得事例あり','扶養控除内','動画ファイル名','給与/交通費　給与下限','対象者設定　性別','WEB登録OK','応募先　備考','オフィスが禁煙・分煙','応募先　所在地　市区町村','仕事写真（下）　写真1　コメント','勤務地　市区町村コード','（派遣先）職場の雰囲気','未使用.13','（紹介予定）待遇・福利厚生','勤務地　最寄駅1（駅名）','勤務地　最寄駅2（分）','応募拠点','給与/交通費　備考','残業なし','これまでの採用者例','期間･時間　備考','（派遣先）概要　勤務先名（フリガナ）'] , axis = 1 )
    x = x.fillna(0)
    train_y = pd.read_csv(train_y_file)
    y = train_y['応募数 合計']
    y = y.fillna(0)
    x_array = np.array(x)
    y_array = np.array(y)
    x_train, x_test, y_train, y_test = train_test_split(x_array, y_array, test_size = 0.4,random_state = 0)
    rfr = RandomForestRegressor(random_state = 0)
    rfr.fit(x_train, y_train)
    y_pred = rfr.predict(x_test)
    np.sqrt(mean_squared_error(y_pred, y_test))
    test_x = pd.read_csv(test_x_file)
    test_x = test_x.drop(['職場の様子','（紹介予定）入社後の雇用形態','勤務地　最寄駅3（駅名）','勤務地固定','休日休暇(月曜日)','応募先　名称','（派遣先）配属先部署　男女比　男','勤務地　最寄駅3（沿線名）','（派遣先）勤務先写真コメント','勤務地　最寄駅3（分）','無期雇用派遣','勤務地　最寄駅2（駅名）','未使用.14','（派遣以外）応募後の流れ','（派遣先）概要　従業員数','電話応対なし','（紹介予定）雇用形態備考','週払い','週1日からOK','（派遣先）配属先部署　人数','固定残業制 残業代 下限','残業月20時間以上','職種コード','1日7時間以下勤務OK','ミドル（40〜）活躍中','ルーティンワークがメイン','未使用.11','短時間勤務OK(1日4h以内)','フリー項目　内容','先輩からのメッセージ','対象者設定　年齢下限','未使用.10','土日祝のみ勤務','掲載期間　開始日','動画コメント','Wordのスキルを活かす','未使用.8','経験必須','固定残業制 残業代に充当する労働時間数 下限','給与/交通費　給与支払区分','ブロックコード2','未使用.4','CAD関連のスキルを活かす','未使用.7','お仕事No.','メモ','派遣スタッフ活躍中','ブロックコード3','WEB面接OK','公開区分','17時以降出社OK','寮・社宅あり','20代活躍中','Accessのスキルを活かす','検索対象エリア','就業形態区分','ネットワーク関連のスキルを活かす','Wワーク・副業可能','勤務地　最寄駅2（沿線名）','休日休暇(火曜日)','固定残業制 残業代に充当する労働時間数 上限','プログラム関連のスキルを活かす','未使用.15','平日休みあり','（派遣先）概要　勤務先名（漢字）','勤務地　最寄駅2（駅からの交通手段）','休日休暇　備考','30代活躍中','フラグオプション選択','未使用.12','エルダー（50〜）活躍中','（派遣）応募後の流れ','期間・時間　勤務時間','期間・時間　勤務期間','人材紹介','週2・3日OK','主婦(ママ)・主夫歓迎','勤務先公開','Excelのスキルを活かす','16時前退社OK','正社員登用あり','残業月20時間未満','勤務地　備考','拠点番号','雇用形態','Dip JobsリスティングS','ブロックコード1','フリー項目　タイトル','（紹介予定）入社時期','お仕事名','資格取得支援制度あり','未使用.1','ブランクOK','対象者設定　年齢上限','未使用.20','10時以降出社OK','募集形態','期間・時間　勤務開始日','英語以外の語学力を活かす','勤務地　最寄駅3（駅からの交通手段）','外資系企業','（派遣先）勤務先写真ファイル名','応募先　最寄駅（沿線名）','仕事写真（下）　写真1　ファイル名','PowerPointのスキルを活かす','未使用.16','仕事写真（下）　写真3　ファイル名','オープニングスタッフ','応募先　所在地　ブロックコード','（派遣先）配属先部署','（派遣先）配属先部署　男女比　女','応募先　所在地　都道府県','動画タイトル','仕事内容','（派遣先）概要　事業内容','応募先　最寄駅（駅名）','残業月10時間未満','休日休暇(土曜日)','（紹介予定）年収・給与例','外国人活躍中・留学生歓迎','履歴書不要','未使用.17','休日休暇(木曜日)','未使用.9','日払い','未使用','勤務地　最寄駅1（沿線名）','未使用.18','未使用.22','未使用.5','（派遣先）配属先部署　平均年齢','英語力を活かす','勤務地　周辺情報','仕事写真（下）　写真2　ファイル名','バイク・自転車通勤OK','仕事写真（下）　写真2　コメント','DTP関連のスキルを活かす','会社概要　業界コード','未使用.3','PCスキル不要','車通勤OK','制服あり','給与/交通費　給与上限','休日休暇(水曜日)','未使用.2','WEB関連のスキルを活かす','仕事の仕方','未使用.6','給与　経験者給与下限','勤務地　最寄駅1（駅からの交通手段）','応募資格','学生歓迎','紹介予定派遣','固定残業制 残業代 上限','未使用.19','（紹介予定）休日休暇','給与　経験者給与上限','シフト勤務','経験者優遇','週4日勤務','派遣会社のうれしい特典','土日祝休み','給与/交通費　交通費','掲載期間　終了日','未使用.21','待遇・福利厚生','シニア（60〜）歓迎','ベンチャー企業','少人数の職場','仕事写真（下）　写真3　コメント','新卒・第二新卒歓迎','休日休暇(金曜日)','お仕事のポイント（仕事PR）','産休育休取得事例あり','扶養控除内','動画ファイル名','給与/交通費　給与下限','対象者設定　性別','WEB登録OK','応募先　備考','オフィスが禁煙・分煙','応募先　所在地　市区町村','仕事写真（下）　写真1　コメント','勤務地　市区町村コード','（派遣先）職場の雰囲気','未使用.13','（紹介予定）待遇・福利厚生','勤務地　最寄駅1（駅名）','勤務地　最寄駅2（分）','応募拠点','給与/交通費　備考','残業なし','これまでの採用者例','期間･時間　備考','（派遣先）概要　勤務先名（フリガナ）'] , axis = 1 )
    test_x = test_x.fillna(0)
    test_x_array = np.array(test_x)
    answer_y = rfr.predict(test_x_array)
    osigoto_no = pd.read_csv(test_x_file2)
    osigoto_no = osigoto_no['お仕事No.']
    osigoto_no = pd.DataFrame(osigoto_no)
    answer_y = pd.DataFrame(answer_y)
    osigoto_no['応募数　合計'] = answer_y
    csv = osigoto_no.to_csv(index=False)  
    csv_financde = osigoto_no.to_csv(index = False).encode('Shift-JIS')
    st.download_button(
        label='CSVダウンロード',
        data=csv_financde,
        file_name='result.csv',
        mime='text/csv'
    )
