import json
import requests

import csv
import concurrent.futures


cookies = {
    "gdId": "192d72d9-70d3-4741-a5a9-fada22e67cc3",
    "indeedCtk": "1hb1m092a2ejv001",
    "rl_page_init_referrer": "RudderEncrypt%3AU2FsdGVkX19h5xY690awn5mAnNUUL%2F7tTExYfl8hHDbCoRr7EKeLq2WR5A601TIP",
    "rl_page_init_referring_domain": "RudderEncrypt%3AU2FsdGVkX1%2B8UVNWvz35V4ZrbDysv6l8rmcFLP7UcxTZOwmmcdP1I%2FwCNgEZaCiP",
    "_ga": "GA1.2.181885389.1695494984",
    "_optionalConsent": "true",
    "_gcl_au": "1.1.1537180418.1695494985",
    "_rdt_uuid": "1695494986584.cbcbdb00-c66e-4507-9b1e-ed60d56efdc4",
    "__pdst": "0e021f3d73b648b88bb91c860a6c1104",
    "_fbp": "fb.1.1695494987048.828068691",
    "G_ENABLED_IDPS": "google",
    "_tt_enable_cookie": "1",
    "_ttp": "5US4zDimzCmuo80hSjW9CM5sR-g",
    "_cfuvid": "Tr5aFMs9xnOTBBkXgcLyEryewRWFGcbzb0l3u7ipCl4-1697890563155-0-604800000",
    "GSESSIONID": "undefined",
    "_gid": "GA1.2.2030792600.1697890578",
    "cass": "1",
    "_pin_unauth": "dWlkPVltWXpPRE00TkdJdE1HTXhOeTAwWXpReExUa3hOVE10WWpJNE4yRXdPV00xTUdRdw",
    "ki_r": "",
    "g_state": '{"i_p":1697977889014,"i_l":2}',
    "uc": "8013A8318C98C517CF968C3EE416FDA4ADBF0CE16917CA83B24922AD8280B49B8F1CCDB9A4DE79AF9384C21DA23C8C8A8F256250A351DF8AA2A63F4F06DAE97D19A1ACA40F0423AC1E4E4138D878BC1E92C650DF0DC70D99DF6FC6869F414FD1E8133092DB8A865CDD82F014941C4FF2F925DA809B9343D0270D2416CF1FE1BFA65FE2F6B9183782B963352C312BABD4",
    "G_AUTHUSER_H": "1",
    "trs": "INVALID:SEO:SEO:2022-04-28+20%3A29%3A13.797:undefined:undefined",
    "asst": "1697895294.0",
    "JSESSIONID": "6F88FEAC83E7A0658CB6CC2D049801A0",
    "rsSessionId": "1697895301413",
    "__cf_bm": "rqEECTfIrot3fFBuWybynsLCLb9MNJbLrPoJIwYgdO0-1697898920-0-AcFJq0/yYK6tSdtSHv0wtB/RGrB+PsIzB8ppv1NBczJhsZX/wXQgUe+91O4UTlFrlRvO7aQtLOj8rocg3b/tLB7iHcuEWA9iiQQvQFsujXr2",
    "gdsid": "1697890570388:1697900379253:4D0345153A4185B049603FFE3AC2100B",
    "at": "taJzxBCA99prBSrLZ9qNmnC3dK8JYGpzjs7UUKIE3-Z9mSa8zZcg9BeV0OTc2nkiEXRv33qRmxwi6W3DRbmxcKFhLQHVbK9CcqnunBOsmjhRXAKg01yFGjmVIQq-1UKjOA4h23lkUNwbgUD7GY8nRnvM3io1dzogkPx8qJsHR9sV2BAMdWEOWYlqOlR4PvrwEfoT7Uo9Qw0mwPvJf5rtFuSH-bgjQi2aZyxz9_CknwYum7XPZEIdyaNAcwaobnYERx2jSYKSjQQE5xZFsSWxP8HzYJr_WcU48Vkmt9PXd7MMQs9jOQpZ0Ay4AtJLSKesUpNdnQtBKJ_PDDH1T0b9eBvbBjj3yVqUJBwWviOXTTrzMylVFQUy5xmAuUwfsvpgGWtwLrF_Z2y7HFzmiiJNHLNJ2liwSxMvYZ6xlsfMtts69HwX_1rvUnkSQVZAwpnBpCu3LUHaegYsGsik4Iay_zTxp_sBvv9FhBz5odGrBLnZ_5_RFj3mwma2W7vykig_4vYWGCr9YNj6jLTJwmXU1a_yo922UQvtO7KSjN12pRAu3qvOb-C6sPu8XW2RMBEp6rs0n_btmDnCCIeBQhnCgBOBMYy2PaWtnPPn90fYhZQpNiRRYjmID2twgvvbF2DNY0LUvXYOSvCBghtGpFQzhienTijS2JMp9uEkkEovSm8vOXxFhaRpGZQOS8_ksSPUZhJ-hfJtam88iC7rbx9NJ5Z_0joR1q8QyeyAVajD0r8YgdBBdjVIBnzY9CC8EFz2ZMM9j02Tgs-n0vT4BpgIzJSsmkPJkWhZWOWDVPrjHIB-WDmd93Emzh66zrAljXK1g9EUVp6o0x-mGsSWLHo8VHGzNlLu1oi3n4xDLgXd_br32AvZckfpaoiqlMNj6Z2o0p8",
    "_dd_s": "rum=0&expire=1697901331141",
    "rl_user_id": "RudderEncrypt%3AU2FsdGVkX19oRBSx0nMw0%2BSjo6Vrq%2F%2Fxz0mrne3%2BtY4%3D",
    "rl_trait": "RudderEncrypt%3AU2FsdGVkX1%2FUn5aoA3prqQxWeHo1jrxfcMuA51mvRVg0rbIKIdT1EJBOyn%2BMjYqCisOMzpw8Lk8phLb6MsG8%2Bz1Gmd%2BlTd8qBjlKXJ%2BMpsjVH2XBzZmnHoZdDCbeUtx8BtewpzQ6IkHhEu4H%2FqP2G330yCE4CKUy5C9NfcRqTT9mcJjO7gEhCgE%2B9jYSD1gnQ8YaTba%2BTpLa3Qvx5Ql34y7%2FkVDI%2BZDyLdLOH%2B65%2FQw%3D",
    "rl_group_id": "RudderEncrypt%3AU2FsdGVkX1%2BSAW2WIUQ%2FdQQoIF9FWMjmHeLp4JATkYk%3D",
    "rl_group_trait": "RudderEncrypt%3AU2FsdGVkX182%2FmcySM2tr8mjJoSvItS0MIzPHsZ0NOw%3D",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Sat+Oct+21+2023+20%3A00%3A53+GMT%2B0500+(Pakistan+Standard+Time)&version=202306.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=184bca11-e819-466e-887d-5c9773b3c96b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CC0017%3A1&AwaitingReconsent=false",
    "ki_t": "1697890587156%3B1697890587156%3B1697900460493%3B1%3B7",
    "ki_u": "024332bc-edab-b0fa-c8e6-d993",
    "ki_s": "218147%3A1.0.0.1.2",
    "bs": "gphxzq0fhuYGhtN_XyFa4w:3PRk0bkWfDo23G7eSLqQhQFWLBGZ66hNg7zdvMC0TK_ZWD69uL4FL_9tRvf9nYxA_1Z5lD7tvdio-l4TdBdLgRUpXBbxx0DCl7_Bv4ZVtj0:Wuo7PIjAQVja2VehV5-ldqreZDpnQS_c83kUJdfaM_s",
    "_dc_gtm_UA-2595786-1": "1",
    "rsReferrerData": '{"currentPageRollup":"/reviews/reviews","previousPageRollup":"/reviews/reviews","currentPageAbstract":"/Reviews/[EMP]-Reviews-E[EID]_[PRM].htm","previousPageAbstract":"/Reviews/[EMP]-Reviews-E[EID]_[PRM].htm","currentPageFull":"https://www.glassdoor.com/Reviews/Meta-Reviews-E40772_P7.htm?filter.iso3Language=eng","previousPageFull":"https://www.glassdoor.com/Reviews/Meta-Reviews-E40772_P5.htm?filter.iso3Language=eng"}',
    "rl_anonymous_id": "RudderEncrypt%3AU2FsdGVkX1%2FJKqNs59CnhwktVc3psA0WPF%2FCGzHkon5Nv37ouAe6kPGT7tDmj%2BhFaRreVLANX%2FhWE9tSbrU71A%3D%3D",
    "rl_session": "RudderEncrypt%3AU2FsdGVkX1%2BNgC5YrFZONJiMYbdo0cYUNa8BsIKx%2BZOQREU42PCOnJEizhQkwlI6zhjZGT%2FIUhRN4E6%2Fe%2FQXXk0lad%2B01DZhicL6nHIGMIicrSImpUuU2lOj55zumYzpk2wHtoU6%2FIUAgS7T8iH9Kw%3D%3D",
    "AWSALB": "4eDEh43GKKzXtUoefthIdr9qdxj/9eYigQdH/LLqWurNZM2ZptZiyXlfj39Yx2VYW2Ob4Nf/MbgwfkuPxJCDmCdt9P5+bBu6cySBw2dz8B0uMrftAFLuS+cpKlfr",
    "AWSALBCORS": "4eDEh43GKKzXtUoefthIdr9qdxj/9eYigQdH/LLqWurNZM2ZptZiyXlfj39Yx2VYW2Ob4Nf/MbgwfkuPxJCDmCdt9P5+bBu6cySBw2dz8B0uMrftAFLuS+cpKlfr",
    "fpvc": "2",
}

headers = {
    'authority': 'www.glassdoor.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'apollographql-client-name': 'company.explorer',
    'apollographql-client-version': '3.18.8',
    'content-type': 'application/json',
    # 'cookie': 'gdId=192d72d9-70d3-4741-a5a9-fada22e67cc3; indeedCtk=1hb1m092a2ejv001; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19h5xY690awn5mAnNUUL%2F7tTExYfl8hHDbCoRr7EKeLq2WR5A601TIP; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2B8UVNWvz35V4ZrbDysv6l8rmcFLP7UcxTZOwmmcdP1I%2FwCNgEZaCiP; _ga=GA1.2.181885389.1695494984; _optionalConsent=true; _gcl_au=1.1.1537180418.1695494985; _rdt_uuid=1695494986584.cbcbdb00-c66e-4507-9b1e-ed60d56efdc4; __pdst=0e021f3d73b648b88bb91c860a6c1104; _fbp=fb.1.1695494987048.828068691; G_ENABLED_IDPS=google; _tt_enable_cookie=1; _ttp=5US4zDimzCmuo80hSjW9CM5sR-g; _cfuvid=Tr5aFMs9xnOTBBkXgcLyEryewRWFGcbzb0l3u7ipCl4-1697890563155-0-604800000; GSESSIONID=undefined; _gid=GA1.2.2030792600.1697890578; cass=1; _pin_unauth=dWlkPVltWXpPRE00TkdJdE1HTXhOeTAwWXpReExUa3hOVE10WWpJNE4yRXdPV00xTUdRdw; ki_r=; g_state={"i_p":1697977889014,"i_l":2}; uc=8013A8318C98C517CF968C3EE416FDA4ADBF0CE16917CA83B24922AD8280B49B8F1CCDB9A4DE79AF9384C21DA23C8C8A8F256250A351DF8AA2A63F4F06DAE97D19A1ACA40F0423AC1E4E4138D878BC1E92C650DF0DC70D99DF6FC6869F414FD1E8133092DB8A865CDD82F014941C4FF2F925DA809B9343D0270D2416CF1FE1BFA65FE2F6B9183782B963352C312BABD4; G_AUTHUSER_H=1; trs=INVALID:SEO:SEO:2022-04-28+20%3A29%3A13.797:undefined:undefined; ki_u=024332bc-edab-b0fa-c8e6-d993; ki_s=218147%3A1.0.0.1.2; fpvc=3; companiesClicked=true; JSESSIONID=79B33D595344FE6736CC61AA56561164; asst=1697909645.0; __cf_bm=9lFZ5lSgB8yGy_LiGaGxyITUwG7D.LhItCO5IL55PQQ-1697909646-0-ARFVC/E7hEZgpSJtWN+LhioYkpanQtMVzSapnhDDOP455jU+188zRGFAnZj4oekJV1pZr6+BqE43hU1NIqW7dRUladayygVQUyVOutqQ2UJX; rsSessionId=1697909860521; AWSALB=+T2FCyRI+8entYYhhuwUN79y+PsYhI/6vpfTK8dOEnagHqH7b2vwPU1KKHdQHwL8qG/iT6v5GxMV2D4xLTWcKtD/HXhP8+CBbWnrDZX6Lh/ZRB1XjGq/dZRC26V2; AWSALBCORS=+T2FCyRI+8entYYhhuwUN79y+PsYhI/6vpfTK8dOEnagHqH7b2vwPU1KKHdQHwL8qG/iT6v5GxMV2D4xLTWcKtD/HXhP8+CBbWnrDZX6Lh/ZRB1XjGq/dZRC26V2; at=a4fm9_lBhpUKEBH_BmcJPZ86kDKajGjdzT78O5jYq7U3gL8BLyAOaEctXc0Ty8vLYHm2IH5-dh4iZeKktIMd42c4I4CpJ-PDlgZsqsiPLTZGJrGWjgXp9eyrYDGnwWwrCvO4Hort4PAmDy9-Q8ykDBxEgJhA0lJFC1b-NwjmwrdBhOsqF-9w3Uo_sZxFUJyaN93c08vQDMaS3YeX9PqD0d_0jnyR-Con5iE99w5X6ndi98wjqVoWEmjVzfsqg6yze3qilPoLlY0JYmpM7Ifu5DhbLGv8Ph41_zxxrYsiggv8FHp7I7rvirPTL4YZZq3qNPPksxSFDqjW3bLXIZCpWHOQZP1eyowPvB-uG2otT8SMVRfP_Ct5Bh5uYwpOczqnJaUNXFQx0QwbU31MztqNNnNk65baKMdmIRdYtJGkhzbbqJ9BJ9Pl-ZO7atECPdGiiqxLIQNjow0mxI6kwE1E5pDSSVYG-zCXgVE_BuHB9GpbPEkxos4PRhLDp7YjRsxuSurEpcRoryfRY1gznRiEHWSwCM4Hv26jHr609HNX1HV8qhDNJskdCZgpNYbg_uR1N45GAX8GBSI0ZyRpAP6iRrnzrwElchu-hH-iKzHbnlLJGeizS_hijyqCkkIbnEZQwLe1gTAWWGeNmIi6jexOQ0RUC_7xWDHX3hL9iZRS5Bp06AvyY66n10fqGJlXpYkBslac29c3Del9xP8WkAxEt8ss2254lLvTRNYLIQpASLcDk5Wn_NxHJcCK5ISIHXDz4N4lVopTOwMeTGEBWu6T5jubwu_B5Y2h77rj0RpJD_n8rkGooje8bN0xzFqV1TWFEPPnnWIpZWjotfHMot5ojxYVc23Rgtdu7DCR9ICzHXSiu3HZ_hjCu34e0LaPPQOIB14; gdsid=1697890570388:1697910870223:D79BE79D7469F7B3EECD1C51146664F6; rl_user_id=RudderEncrypt%3AU2FsdGVkX19P0Dj7FMuYICmUPYS36vvMRKjaHHmCKpY%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX18onxxnhuX6%2BXiNxfF6NtFOg35TfnoFJ0sjAvYL%2BVMldNO1S2eKD3RGY51beD%2FWqCpTx%2BNvv%2BPTU95VdNstjFj4R789UkhJubwpMlucOFRVry5yydmawyz1fuqxofJHQzWSEvMu%2FcEh5teo9oCFW8I0zunYN0BVA%2F29K6NIMhHMMBz94lu9VnsX5ZpjfhPIAuRpfL2KweAM5A2XNeFrBasjkOzaRKozUJs%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX18Ajf4QkYXjw6d7kbvBw1kGaDdPjAMkui8%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX19NY4%2BODaWzN3aIarmNIo%2FGlWWewMRlkfQ%3D; rsReferrerData={"currentPageRollup":"/reviews/index","previousPageRollup":"/reviews/index","currentPageAbstract":"/Reviews/index.htm","previousPageAbstract":"/Reviews/index.htm","currentPageFull":"https://www.glassdoor.com/Reviews/index.htm?overall_rating_low=2.5&page=100&filterType=RATING_OVERALL","previousPageFull":"https://www.glassdoor.com/Reviews/index.htm?overall_rating_low=2.5&page=999&filterType=RATING_OVERALL"}; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX18Ub79tlYnqg2Wbg%2BVHN%2BeaqQXp5KvkGWaHWlyhXPogybp6yVMRESCiidX2tNhkA444iMQy4NO5WQ%3D%3D; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Oct+21+2023+22%3A57%3A21+GMT%2B0500+(Pakistan+Standard+Time)&version=202306.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=184bca11-e819-466e-887d-5c9773b3c96b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CC0017%3A1&AwaitingReconsent=false; ki_t=1697890587156%3B1697890587156%3B1697911049567%3B1%3B30; bs=RFovj4oE9z3FPzBW6zs1Zw:UNL8JS3mbmimFdJys1fBd6egzxe-VATNoqfmzWRKPfnp_Sxj04e1_4cs7dS95Fh0DD7yDnwjeDputmDjL1z3-BPQnO7lKH4mICU0FneKSt8:7pcOZmuf40Y51rpQMbCAzgnV4aiyBxTqirvnkZaR2K0; rl_session=RudderEncrypt%3AU2FsdGVkX18vbIm1Ywgn20%2Be3jVuKg5a34BJjr6X5IEiF3nnc37wtOY1L12dn2o%2FA%2Bw8MnMZHFfjTLpTvBVjWCKRg1viQSOxxcPe6dWG24V9EU8nH8rvbucqFdjJt4gsKIqq0dDf9Yv2nXVaOyO22A%3D%3D; _dc_gtm_UA-2595786-1=1',
    'gd-csrf-token': 'JJjPxTaHC71mEs5g7FYeig:nxwD84kMLSbuVcKjYWPskWSzNN0BpN9TxqbdAAyRutPqUxxAehkLMiyY6LcheLBBWalsTcWVoRAFgPp1gwOexg:ESXKcBL09kJ4kAIxrtpfnyHTdeqrTjoIWo62LCtGAeo',
    'origin': 'https://www.glassdoor.com',
    'referer': 'https://www.glassdoor.com/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

companiesQuery = [
    {
        'operationName': 'ExplorerEmployerSearchGraphQuery',
        'variables': {
            'employerSearchRangeFilters': [
                {
                    'filterType': 'RATING_OVERALL',
                    'maxInclusive': 5,
                    'minInclusive': 2.5,
                }
            ],
            'industries': [],
            'jobTitle': '',
            'location': None,
            'pageRequested': 1,
            'preferredTldId': 1,
            'sGocIds': [],
            'sectors': [],
        },
        'query': 'query ExplorerEmployerSearchGraphQuery($employerSearchRangeFilters: [EmployerSearchRangeFilter], $industries: [IndustryIdent], $jobTitle: String, $location: UgcSearchV2LocationIdent, $pageRequested: Int, $preferredTldId: Int, $sGocIds: [Int], $sectors: [SectorIdent]) {\n  employerSearchV2(\n    employerSearchRangeFilters: $employerSearchRangeFilters\n    industries: $industries\n    jobTitle: $jobTitle\n    location: $location\n    pageRequested: $pageRequested\n    preferredTldId: $preferredTldId\n    sGocIds: $sGocIds\n    sectors: $sectors\n  ) {\n    employerResults {\n      demographicRatings {\n        category\n        categoryRatings {\n          categoryValue\n          ratings {\n            overallRating\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      employer {\n        bestProfile {\n          id\n          __typename\n        }\n        id\n        shortName\n        ratings {\n          overallRating\n          careerOpportunitiesRating\n          compensationAndBenefitsRating\n          cultureAndValuesRating\n          diversityAndInclusionRating\n          seniorManagementRating\n          workLifeBalanceRating\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    numOfPagesAvailable\n    numOfRecordsAvailable\n    __typename\n  }\n}\n',
    },
]

companySizeRanges = [
    {
        "filterType": "EMPLOYEES_COUNT", 
        "minInclusive": 1, 
        "maxInclusive": 50
    },
    {
        "filterType": "EMPLOYEES_COUNT", 
        "minInclusive": 51, 
        "maxInclusive": 200
    },
    {
        "filterType": "EMPLOYEES_COUNT", 
        "minInclusive": 201, 
        "maxInclusive": 500
    },
    {
        "filterType": "EMPLOYEES_COUNT", 
        "minInclusive": 501, 
        "maxInclusive": 1000
    },
    {
        "filterType": "EMPLOYEES_COUNT", 
        "minInclusive": 1001, 
        "maxInclusive": 5000
    },
    {
        "filterType": "EMPLOYEES_COUNT", 
        "minInclusive": 5001, 
        "maxInclusive": 10000},
    {
        "filterType": "EMPLOYEES_COUNT",
        "minInclusive": 10001,
        "maxInclusive": 9007199254740991,
    },
]

file = open('companies_data.csv', mode='a', newline='', encoding='utf-8')
writer = csv.DictWriter(file, 
                    fieldnames=['CompanyID', 'CompanyName', 'CompanySize'])
# writer.writeheader()

def Glassdoor_Companies(pageRequested: int, companySizeRange: dict):
    companiesQuery[0]['variables']['employerSearchRangeFilters'].append(companySizeRange)
    companiesQuery[0]["variables"]['pageRequested'] = pageRequested

    response = requests.post(
        "https://www.glassdoor.com/graph", 
        headers=headers, 
        json=companiesQuery
    )

    print("Status Code:", response.status_code)
    print("Number of page:", pageRequested)
    responseData = json.loads(response.text)
    extract_companies_data = responseData[0]["data"]["employerSearchV2"]["employerResults"]



    for company in extract_companies_data:
        CompanyName = company["employer"]["shortName"]
        CompanyID = company['employer']['id']
        CompanySize = json.dumps(companySizeRange)

        writer.writerow({
            'CompanyID': CompanyID,
            'CompanyName': CompanyName,
            'CompanySize': CompanySize
        })


# Glassdoor_Companies(2, companySizeRanges[0])


num_threads = 4  # You can adjust this to your needs
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    # List of input pairs (input1, input2)
    inputs = [(requestedPage, companySizeRanges[5]) for requestedPage in range(1, 466)]

    # Submit tasks to the thread pool and store the futures in a list
    futures = [executor.submit(Glassdoor_Companies, input1, input2) for input1, input2 in inputs]

    # Wait for all tasks to complete and retrieve the results
    results = [future.result() for future in futures]


# all_reviews = data[0]['data']['employerReviews']['reviews']

# for review in all_reviews:
#     reviewDateTime = review['reviewDateTime']
#     ratingOverall = review['ratingOverall']
#     ratingWorkLifeBalance = review['ratingWorkLifeBalance']
#     ratingCultureAndValues = review['ratingCultureAndValues']
#     ratingDiversityAndInclusion = review['ratingDiversityAndInclusion']
#     ratingSeniorLeadership = review['ratingSeniorLeadership']
#     ratingRecommendToFriend = review['ratingRecommendToFriend']
#     ratingCareerOpportunities = review['ratingCareerOpportunities']
#     ratingCompensationAndBenefits = review['ratingCompensationAndBenefits']

#     print(reviewDateTime)
