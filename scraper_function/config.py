"""
This file contains the config values for the 
geocaches scraper function
"""
table_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0)' +
    ' Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.geocaching.com/' +
    'play/results/?st=singapore&ot=query&asc=true&sort=distance',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

table_params = {
    'skip': '0',
    'take': '2000',
    'asc': 'true',
    'sort': 'distance',
    'properties': 'callernote',
    'rad': '16093.44',
    'origin': '1.36692,103.80129',
    'dorigin': '1.38179,103.76864',
}

desc_headers = {
    'Accept': 'text/html,application/xhtml+xml,' +
    'application/xml;q=0.9,image/avif,image/webp,image/apng,' +
    '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Referer':
    'https://www.geocaching.com/play/results/?st=singapore&ot=query&asc=true&sort=distance',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ' +
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}
# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long
table_cookies = {
    '__RequestVerificationToken':
    'Qb6tBP1PANOX03-a4pmIJ4OXSM6FZNLpv8qguG2WigEO8Li8h6q4VVllnsfVTKD0zMpXwr51OHhdO_9hgMd-O3Tssk01',
    'CookieConsent':
    '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:3%2Cutc:1685073602122%2Cregion:%27SG%27}',
    '_ga': 'GA1.1.46338098.1685073610',
    '_gid': 'GA1.2.806380753.1685073610',
    '_ga_GRQE2910DL': 'GS1.1.1685073610.1.1.1685073678.0.0.0',
    'gspkauth': '-WVnE3ot2-85Q51qj9CcI1g8Gn-1X-VAm85k8u9h5ilX' +
    'OwDDKtf6LbGYfSjvVsQ42y1oXoQugr00xEvA7F' +
    '_JODCAGK37686OM5mlHC9-qa2S9kLOGeuTWXhTLvj_wj2T7Wh-vPQ2SCzpyXojFCrxVUYIXE7goZ7ltdRYLjVGPrE1',
    '_hjSessionUser_441815': 'eyJpZCI6IjQ0OWI1YjY2LTVhNzQtNWZ' +
    'jMy04ZWM3LTc1YTJmODk5MGRjOSIsImNyZWF0ZWQiOjE2ODUwNzM2MTE5NzQsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_441815': '1',
    '_hjSession_441815': 'eyJpZCI6ImJkODhlYmQ2LTNkYzY' +
    'tNGZhYi04OTBlLWE0Mjg1ZGZlZWQxZSIsImNyZWF0ZWQiOjE2ODUwNzM2MTM2NTAsImluU2FtcGxlIjp0cnVlfQ==',
    '_hjAbsoluteSessionInProgress': '0',
    'jwt': 'eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctb' +
    'W9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bW' +
    'xzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoib3Jlb3BpZz' +
    'EyMyIsInBnZCI6IjAxNTFlZmUxLTY3ZDQtNDJlYy04MTMzLTBmOTZmYjY4YTUxOSIsImh0dH' +
    'A6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZ' +
    'GVudGlmaWVyIjoiMjUxNTA2ODciLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMD' +
    'gvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOlsiUHVibGljIiwiQmFzaWMiXSwiaHR0cDovL3NjaGVtY' +
    'XMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy91c2VyZGF0YSI6IjFFOUMwN' +
    'EY3LTYzMEItNDZGMy04NUM1LUVFMDhDMDk4NkQ2NiIsImxnZCI6IjM2YTcwNjQ5LWQ5ZTktNDM3OS05ZjY' +
    'xLWNjMDBlOTIwNWU5NCIsInNjb3BlIjpbIndlYiIsIm1hcHRpbGUiLCJnYXJtaW4iXSwibmJmIjoxNjg1MDcz' +
    'NjMwLCJleHAiOjE2ODUwNzcyMzAsImlzcyI6Imh0dHBzOi8vb2F1dGguZ2VvY2FjaGluZy5jb20vdG9rZW4iLCJ' +
    'hdWQiOiIxZTljMDRmNy02MzBiLTQ2ZjMtODVjNS1lZTA4YzA5ODZkNjYifQ.FQODn5k_YDSWM3ZQ6ewAV3-J_M7_' +
    'Cs-pHaODAbixqOk',
    '_csrf': 'Bx94HmybGf7KQRBR56NiNp21',
    'ai_user': 'xMcjS2M0t5aCk04vyLYpeM|2023-05-26T04:00:27.717Z',
    'ai_session': 'FtI++1lUqDpfM+uTd1Y8eY|1685073628724|1685073679556',
}

desc_cookies = {
    'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:3%2Cutc:1685074395221%2Cregion:%27SG%27}',
    '_gid': 'GA1.2.883987124.1685074399',
    '_hjSessionUser_441815': 'eyJpZCI6IjI0Y2IxOTQ4LTkyOGQtNTA2MC05Z' +
    'jk1LWEwZGZkNGZmNjRmYyIsImNyZWF0ZWQiOjE2ODUwNzQ0MTczMTMsImV4aXN0aW5nIjp0cnVlfQ==',
    '__RequestVerificationToken': 'cWHz0d0y5TgAVjADnDpZBvL9M8JaRKL_6VNwNj-' +
    'pGs1Q0KrezO2EtntJ9Qpz8FF6j3YJ9bdXkzF8UY3v4t0Dfqh4IK41',
    '_hjIncludedInSessionSample_441815': '1',
    '_hjSession_441815': 'eyJpZCI6IjU0OTRlNGZkLTJjMmQtNGIxMS1iNWRiLTk' +
    '5NDQ1MTM3YmM2YiIsImNyZWF0ZWQiOjE2ODUxMTY0MTMzOTksImluU2FtcGxlIjp0cnVlfQ==',
    '_csrf': 'a3IStaKrwfJANLgIZTw3HJC4',
    'ai_user': 'zjjBTlW1TrbfQxMFBMpKIO|2023-05-26T15:54:12.297Z',
    'Culture': 'en-US',
    'gspkauth': 'JZrkgg0HerbRHsFf2-orQCqf6EQkzF6slWNb2pxVzQ0SBdVK6W1nIPNufF2i' +
    'ikd1ByVKntwzNeOPYw1MTHq-tsRcy1MpVMNS3GWYy0cRFW_Cakxr45J-RSYYm-rbq4K0lBMvps' +
    'QbjdBkcDYV_H2SmgsWWmYzGizXZdy9DHAAQXw1',
    '__gads': 'ID=290e87d311cae4e3:T=1685074404:RT=1685116476:S=ALNI_MZ-IlYAWrtnYwm7KtqNg4xZK87F9Q',
    '__gpi': 'UID=00000c0b287fa465:T=1685074404:RT=1685116476:S=ALNI_MZ7lkBBf1D9RlBNQ5xDv-mNFgmABA',
    '_ga_WH86DS6J89': 'GS1.1.1685116390.4.1.1685116880.0.0.0',
    '_ga': 'GA1.1.1168483833.1685074399',
    'ai_session': '7qNqKGeD1eORsSbxWHMm/N|1685116453432|1685116880984',
    'jwt': 'eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobW' +
    'FjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yM' +
    'DA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoib3Jlb3BpZzEyMyIsInBnZCI6IjAxNTFlZmUxLTY' +
    '3ZDQtNDJlYy04MTMzLTBmOTZmYjY4YTUxOSIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzI' +
    'wMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiMjUxNTA2ODciLCJodHRwOi8vc2NoZ' +
    'W1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOlsiUHVibGljIiwiQ' +
    'mFzaWMiXSwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy' +
    '91c2VyZGF0YSI6IjFFOUMwNEY3LTYzMEItNDZGMy04NUM1LUVFMDhDMDk4NkQ2NiIsImxnZCI6IjM2YTcwNjQ5' +
    'LWQ5ZTktNDM3OS05ZjYxLWNjMDBlOTIwNWU5NCIsInNjb3BlIjpbIndlYiIsIm1hcHRpbGUiLCJnYXJtaW4iXS' +
    'wibmJmIjoxNjg1MTE2ODgxLCJleHAiOjE2ODUxMjA0ODEsImlzcyI6Imh0dHBzOi8vb2F1dGguZ2VvY2FjaGluZy5' +
    'jb20vdG9rZW4iLCJhdWQiOiIxZTljMDRmNy02MzBiLTQ2ZjMtODVjNS1lZTA4YzA5ODZkNjYifQ.cWGSKwV' +
    'NIHmGpYvihLlYXDilU5-fKq6SCmKQ8KdVw8M',
    '_gcFilterView': 'treasure=closed&attributes=closed&hiddenBy=closed&placedDate=closed' +
    '&hasCorrectedCoordinates=closed&showPremiumCaches=closed',
    '_ga_GRQE2910DL': 'GS1.1.1685116387.4.1.1685116920.0.0.0',
}
