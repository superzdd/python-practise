def continue_crawl(search_history,target_url):
    if search_history[-1] == target_url:
        return False
    
    if len(search_history) >= 25:
        return False

    if search_history.index(search_history[-1]) < (len(search_history)-1):
        return False
    
    return True

print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],'https://en.wikipedia.org/wiki/Philosophy'))
print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point','https://en.wikipedia.org/wiki/Philosophy'],'https://en.wikipedia.org/wiki/Philosophy'))
print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point','https://en.wikipedia.org/wiki/Floating_point'],'https://en.wikipedia.org/wiki/Philosophy'))
print(continue_crawl([
'https://en.wikipedia.org/wiki/Floating_point01',
'https://en.wikipedia.org/wiki/Floating_point02',
'https://en.wikipedia.org/wiki/Floating_point03',
'https://en.wikipedia.org/wiki/Floating_point04',
'https://en.wikipedia.org/wiki/Floating_point05',
'https://en.wikipedia.org/wiki/Floating_point06',
'https://en.wikipedia.org/wiki/Floating_point07',
'https://en.wikipedia.org/wiki/Floating_point08',
'https://en.wikipedia.org/wiki/Floating_point09',
'https://en.wikipedia.org/wiki/Floating_point10',
'https://en.wikipedia.org/wiki/Floating_point11',
'https://en.wikipedia.org/wiki/Floating_point12',
'https://en.wikipedia.org/wiki/Floating_point13',
'https://en.wikipedia.org/wiki/Floating_point14',
'https://en.wikipedia.org/wiki/Floating_point15',
'https://en.wikipedia.org/wiki/Floating_point16',
'https://en.wikipedia.org/wiki/Floating_point17',
'https://en.wikipedia.org/wiki/Floating_point18',
'https://en.wikipedia.org/wiki/Floating_point19',
'https://en.wikipedia.org/wiki/Floating_point20',
'https://en.wikipedia.org/wiki/Floating_point21',
'https://en.wikipedia.org/wiki/Floating_point22',
'https://en.wikipedia.org/wiki/Floating_point23',
'https://en.wikipedia.org/wiki/Floating_point24',
'https://en.wikipedia.org/wiki/Floating_point25',
'https://en.wikipedia.org/wiki/Floating_point26',
'https://en.wikipedia.org/wiki/Floating_point27',
'https://en.wikipedia.org/wiki/Floating_point28',
'https://en.wikipedia.org/wiki/Floating_point29',
'https://en.wikipedia.org/wiki/Floating_point30',
],'https://en.wikipedia.org/wiki/Philosophy'))