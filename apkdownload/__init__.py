from Google_play_api.googleplay import GooglePlayAPI
from config.config import LOCALE, TIMEZONE, GOOGLE_PASSWORD, GOOGLE_LOGIN

#########################################################################
# need email and password
# need to login on https://accounts.google.com/b/0/DisplayUnlockCaptcha
# if show up SecurityCheckError when you modify the code
#########################################################################


class apkdownloader():


    def __init__(self, mail,password,locale,timezone):
        self.mail = mail
        self.password = password
        self.locale = locale
        self.timezone = timezone
        self.api = self.initialize_login()

    def initialize_login(self):
        #first login need to use account/password
        api = GooglePlayAPI(self.locale, self.timezone)
        api.login(self.mail, self.password)

        # you can get gsfid and subtoken after login
        gsfId = api.gsfId
        authSubToken = api.authSubToken

        # use id and authSubToken to login

        api.login(None, None, gsfId, authSubToken)

        return api


    def downloadApkByPackageName(self, packagename):

        print('-----Downloading APK-----')
        download = self.api.download(packagename, expansion_files=False)
        with open(download['docId'] + '.apk', 'wb') as apkfile:
            for chunk in download.get('file').get('data'):
                apkfile.write(chunk)

        print('Download successful')


    def searchApkByKeyWord(self, search_word, maximum_search):
        """
        search(self, query, nb_result, offset=None):

        Search the play store for an app.

        nb_result is the maximum number of result to be returned.

        offset is used to take result starting from an index.
        """

        apps = api.search(search_word, maximum_search)

        print('searching....\n')

        for app in apps:
            print(app['docId'])


    def getDetailsByPackName(self, packagename):

        details = self.api.details(packagename)

        #print(details['docId'])
        #print(details['permission'])

        for key, value in details.items():
            print(str(key) + "===" + str(value) + "\n")


    def browseCategories(self):
        """
        get all categories in google play store
        """
        categories = self.api.browse()

        for cate in categories:
            print(cate)


    def getSubListByCategory(self, category):
        """
        get specific sub category  by using categories name
        """
        print("List all app in this category: %s" % category)

        sub_list_app = self.api.list(category)

        for sub_list in sub_list_app:
            print(sub_list)


    def getAppBySubList(self, category, sub_list):
        """
        get app by specific sub_list name
        """
        #example api.list("apps_topselling_free","MUSIC_AND_AUDIO")
        sub_list_app = self.api.list(category, sub_list)

        for app in sub_list_app:
            print(app['docId'])

def main():
    
    test = apkdownloader(GOOGLE_LOGIN,GOOGLE_PASSWORD,LOCALE,TIMEZONE)
    test.downloadApkByPackageName("com.facebook.katana")



if __name__ == '__main__':
    main()
