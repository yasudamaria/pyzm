# ライブラリインポート(conda install seleniumをアナコンダで実行する)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#必要な情報を定義
CHROMEDRIVER = "C:\Chrome_Driver\chromedriver.exe"
DOMAIN_BASE = "https://www.instagram.com/"
LOGIN_ID = "自分のID"
PASSWORD = "自分のパスワード"

#ローカルでchromedriverを使うための関数。最終敵に変数driverに入れて返す
def get_driver():
    driver = webdriver.Chrome(CHROMEDRIVER)
    return driver


#ログイン画面を表示するための関数です。
def do_login(driver):
    login_url = DOMAIN_BASE + "accounts/login/"
    driver.get(login_url)

    #最大10秒までかけて良い
    elem_id = WebDriverWait(driver, 10).until(
        #nameという要素を見つける
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    try:
        #要素の名前が「password」
        elem_password = driver.find_element_by_name("password")

        if elem_id and elem_password:
            # ログインID入力
            elem_id.send_keys(LOGIN_ID)

            # パスワード入力
            elem_password.send_keys(PASSWORD)


            # ログインボタンを指定
            elem_btn = WebDriverWait(driver, 10).until(
               # Xpathという形式でbutton要素を取り出しています。
                EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))
            )

            actions = ActionChains(driver)
            actions.move_to_element(elem_btn)
            actions.click(elem_btn)
            #上記の処理を実行
            actions.perform()
            #処理を停止
            time.sleep(3)

            perform_url = driver.current_url

            if perform_url.find(login_url) == -1: #ログイン成功したとき
                return True
            else:
                return False                    

        else:
            return False
    except:
        return False 

#zemi.pyを実行したときのみこのコードが動作する
if __name__ == "__main__":
    driver = get_driver()
    login_flg = do_login(driver)

if login_flg is True:  #62
   url = 'https://www.instagram.com/explore/tags/cat/'
   driver.get(url)
   driver.set_window_size(1600, 1200)
   driver.save_screenshot('screenshot.png')
