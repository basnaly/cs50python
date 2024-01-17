def main():
    # Convert user's input to an insensitively case and remove spaces
    file = input('File name: ').strip().casefold()

    # Check if user's input doesn't have '.'
    if file.find('.') == -1:
        print('application/octet-stream')

    else:
        name, extension = file.split('.')
        match extension:
            case 'gif':
                print('image/gif')
            case 'jpg'| 'jpeg':
                print('image/jpeg')
            case 'png':
                print('image/png')
            case 'pdf':
                print('application/pdf')
            case 'txt':
                print('text/plain')
            case 'zip':
                print('application/zip')


main()
