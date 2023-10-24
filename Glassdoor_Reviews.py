


companiesReview = [
    {
        "operationName": "EIReviewsPageGraphQueryRG",
        "variables": {
            "onlyCurrentEmployees": False,
            "employerId": 40772,
            "jobTitle": None,
            "location": {
                "countryId": None,
                "stateId": None,
                "metroId": None,
                "cityId": None,
            },
            "employmentStatuses": [],
            "goc": None,
            "highlight": None,
            "page": 1,
            "sort": "RELEVANCE",
            "applyDefaultCriteria": True,
            "worldwideFilter": False,
            "language": "eng",
            "preferredTldId": 0,
            "dynamicProfileId": 883377,
            "useRowProfileTldForRatings": True,
        },
        "query": "query EIReviewsPageGraphQueryRG($onlyCurrentEmployees: Boolean, $employerId: Int!, $jobTitle: JobTitleIdent, $location: LocationIdent, $employmentStatuses: [EmploymentStatusEnum], $goc: GOCIdent, $highlight: HighlightTerm, $page: Int!, $sort: ReviewsSortOrderEnum, $applyDefaultCriteria: Boolean, $worldwideFilter: Boolean, $language: String, $preferredTldId: Int, $isRowProfileEnabled: Boolean, $dynamicProfileId: Int, $useRowProfileTldForRatings: Boolean) {\n  employerReviews: employerReviewsRG(\n    employerReviewsInput: {onlyCurrentEmployees: $onlyCurrentEmployees, employer: {id: $employerId}, jobTitle: $jobTitle, location: $location, goc: $goc, employmentStatuses: $employmentStatuses, highlight: $highlight, sort: $sort, page: {num: $page, size: 10}, applyDefaultCriteria: $applyDefaultCriteria, worldwideFilter: $worldwideFilter, language: $language, preferredTldId: $preferredTldId, isRowProfileEnabled: $isRowProfileEnabled, dynamicProfileId: $dynamicProfileId, useRowProfileTldForRatings: $useRowProfileTldForRatings}\n  ) {\n    filteredReviewsCountByLang {\n      count\n      isoLanguage\n      __typename\n    }\n    employer {\n      badgesOfShame {\n        id\n        headerText\n        bodyText\n        __typename\n      }\n      bestPlacesToWork(onlyCurrent: true) {\n        bannerImageUrl\n        id\n        isCurrent\n        timePeriod\n        __typename\n      }\n      bestProfile {\n        id\n        __typename\n      }\n      ceo {\n        id\n        name\n        __typename\n      }\n      employerManagedContent(\n        parameters: [{employerId: $employerId, divisionProfileId: $dynamicProfileId}]\n      ) {\n        isContentPaidForTld\n        __typename\n      }\n      id\n      largeLogoUrl: squareLogoUrl(size: LARGE)\n      links {\n        jobsUrl\n        reviewsUrl\n        faqUrl\n        __typename\n      }\n      regularLogoUrl: squareLogoUrl(size: REGULAR)\n      shortName\n      squareLogoUrl\n      website\n      __typename\n    }\n    queryLocation {\n      id\n      type\n      shortName\n      longName\n      __typename\n    }\n    queryJobTitle {\n      id\n      text\n      __typename\n    }\n    currentPage\n    numberOfPages\n    lastReviewDateTime\n    allReviewsCount\n    ratedReviewsCount\n    filteredReviewsCount\n    ratings {\n      overallRating\n      reviewCount\n      ceoRating\n      recommendToFriendRating\n      cultureAndValuesRating\n      diversityAndInclusionRating\n      careerOpportunitiesRating\n      workLifeBalanceRating\n      seniorManagementRating\n      compensationAndBenefitsRating\n      businessOutlookRating\n      ceoRatingsCount\n      ratedCeo {\n        id\n        name\n        title\n        regularPhoto: photoUrl(size: REGULAR)\n        largePhoto: photoUrl(size: LARGE)\n        currentBestCeoAward {\n          displayName\n          timePeriod\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    reviews {\n      isLegal\n      reviewId\n      reviewDateTime\n      ratingOverall\n      ratingCeo\n      ratingBusinessOutlook\n      ratingWorkLifeBalance\n      ratingCultureAndValues\n      ratingDiversityAndInclusion\n      ratingSeniorLeadership\n      ratingRecommendToFriend\n      ratingCareerOpportunities\n      ratingCompensationAndBenefits\n      employer {\n        id\n        shortName\n        regularLogoUrl: squareLogoUrl(size: REGULAR)\n        largeLogoUrl: squareLogoUrl(size: LARGE)\n        __typename\n      }\n      isCurrentJob\n      lengthOfEmployment\n      employmentStatus\n      jobEndingYear\n      jobTitle {\n        id\n        text\n        __typename\n      }\n      location {\n        id\n        type\n        name\n        __typename\n      }\n      originalLanguageId\n      pros\n      prosOriginal\n      cons\n      consOriginal\n      summary\n      summaryOriginal\n      advice\n      adviceOriginal\n      isLanguageMismatch\n      countHelpful\n      countNotHelpful\n      employerResponses {\n        id\n        response\n        userJobTitle\n        responseDateTime(format: ISO)\n        countHelpful\n        countNotHelpful\n        responseOriginal\n        languageId\n        originalLanguageId\n        translationMethod\n        __typename\n      }\n      featured\n      isCovid19\n      topLevelDomainId\n      languageId\n      translationMethod\n      __typename\n    }\n    ratingCountDistribution {\n      overall {\n        _5\n        _4\n        _3\n        _2\n        _1\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  pageViewSummary {\n    totalCount\n    __typename\n  }\n  industryBenchmarkRatings(ratingsInput: {employerId: $employerId}) {\n    overallRating\n    ceoRating\n    recommendToFriendRating\n    businessOutlookRating\n    cultureAndValuesRating\n    careerOpportunitiesRating\n    workLifeBalanceRating\n    seniorManagementRating\n    compensationAndBenefitsRating\n    diversityAndInclusionRating\n    __typename\n  }\n  reviewLocationsV2(employer: {id: $employerId}) {\n    locations {\n      atlasType\n      id\n      name\n      __typename\n    }\n    employerHQLocation {\n      atlasType\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n}\n",
    },
    {
        "operationName": "RecordPageView",
        "variables": {
            "employerId": "40772",
            "metaData": [],
            "pageIdent": "INFOSITE_REVIEWS",
        },
        "query": 'mutation RecordPageView($employerId: String!, $pageIdent: String!) {\n  recordPageView(\n    pageIdent: $pageIdent\n    metaData: {key: "employerId", value: $employerId}\n  ) {\n    totalCount\n    __typename\n  }\n}\n',
    },
]


