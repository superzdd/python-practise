while True:
    try:
        name = int(input('enter name'))
        break
    except:
        print('error')
    finally:
        print('Attemped input')
    
