import MySQLdb
import random


def create_queries(start, stop):
    originating_src_list = ['FREECHARGE', 'SNAPDEAL', 'ONECHECK']
    status_list = ['UNVERIFIED', 'GUEST', 'REGISTERED', 'TEMP']
    bool_list = [0, 1]
    gender_list = ['m', 'f', 'o']
    language_pref_list = ['HINDI', 'ENGLISH']
    create_wallet_status_list = ['CREATED', 'FAILED', 'NOT_CREATED', 'IN_PROGRESS']
    platform_list = ['OTHERS', 'IOS_APP', 'SNAPLITE', 'IOS_TAB', 'WAP', 'ANDROID_TAB', 'WINDOWS_APP', 'ANDROID_APP', 'WEB', 'WINDOWS_TAB']
    for i in xrange(start, stop):
        s = str(i)
        user_id = s
        sd_user_id = i
        fc_user_id = i
        sd_fc_user_id = i
        originating_src = random.choice(originating_src_list)
        is_enabled = random.choice(bool_list)
        email = 'test'+s+'@sd.com'
        password = s
        is_user_set_password = 1
        mobile_number = i
        status = random.choice(status_list)
        is_google_user = 1
        is_facebook_user = 0
        is_email_verified = random.choice(bool_list)
        is_mobile_verified = random.choice(bool_list)
        first_name = 'user'+s
        last_name = 'smith'
        middle_name = 'mark'
        display_name = s
        gender = random.choice(gender_list)
        language_pref = random.choice(language_pref_list)
        purpose = 'revenance'
        created_time = 'NOW()'
        create_wallet_status = random.choice(create_wallet_status_list)
        is_mobile_only = 0
        platform = random.choice(platform_list)
        is_kyc_verified = random.choice(bool_list)
        is_physicaldoc_verified = random.choice(bool_list)
        client_id = s

        query = "INSERT INTO user(user_id, sd_user_id, fc_user_id, sd_fc_user_id, originating_src, is_enabled, email,\
 password, is_user_set_password, mobile_number, status, is_google_user, is_facebook_user, is_email_verified, \
 is_mobile_verified, first_name, last_name, middle_name, display_name, gender, language_pref, purpose, created_time, \
 create_wallet_status, is_mobile_only, platform, is_kyc_verified, is_physicaldoc_verified, client_id) VALUES \
 ('%s', %s, %s, %s, '%s', %s, '%s', '%s', %s, '%s', '%s', %s, %s, %s, %s, '%s', '%s', '%s', '%s', \
 '%s', '%s', '%s', %s, '%s', %s, '%s', %s, %s, '%s');" \
                % (user_id, sd_user_id, fc_user_id, sd_fc_user_id, originating_src, is_enabled, email, password,
                   is_user_set_password, mobile_number, status, is_google_user, is_facebook_user, is_email_verified,
                   is_mobile_verified, first_name, last_name, middle_name, display_name, gender, language_pref, purpose,
                   created_time, create_wallet_status, is_mobile_only, platform, is_kyc_verified,
                   is_physicaldoc_verified, client_id)

        print query
        yield query


def main():
    conn = MySQLdb.connect(host="10.41.118.31",
                           user="imsuser",
                           passwd="Password@123",
                           db="test")
    x = conn.cursor()
    begin, end = 1234500000, 1234500001
    try:
        for query in create_queries(begin, end):
            print query
            x.execute(query)
            conn.commit()
    except MySQLdb.Error:
        conn.rollback()
    conn.close()

if __name__ == '__main__':
    main()
