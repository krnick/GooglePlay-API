# apk-downloader
use google api download apk via python3


Usage:

* Download project

    ```
    git clone https://github.com/krnick/apk-downloader.git
    ```

    ```

* How to use:
    ```
    $ pip3 install apk-downloader
    ```

    ```python
    import apkdownloader
    apk = apkdownloader.apkdownloader(mail,password,locale,timezone)
    apk.download("package.name")
    ```


* Problem solved :

    You need to login on below website before use this package.
    https://accounts.google.com/b/0/DisplayUnlockCaptcha
    If show up SecurityCheckError when you modify the code also need to re-login.

* Function_description:

    * 透過package name 下載 apk
    def downloadApkByPackageName(packagename):


    * 透過搜尋字串，搜尋最接近apk
    def searchApkByKeyWord(search_word, maximum_search):


    * 透過package name 取得apk 細節資訊 
    def getDetailsByPackName(packagename):


    * 取得所有分類
    def browseCategories():


    * 透過大分類取得子分類
    def getSubListByCategory(category):


    * 透過大分類、子分類 取得對應的package name
    def getAppBySubList(category, sub_list):

