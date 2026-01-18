import cv2

print("Hello to my opencsv first program\nThis program is to convert an colourful image into grayscale...")
image = input("Enter your file name:")
flag = False
try:
    image = cv2.imread(image)
    if image is not None:
        print("Image successfully loaded...")
        flag = True
    else:
        print("Image could not be loaded...")
except Exception as e:
    print(e)
finally:
    print("Process 1 Completed...")

if flag:
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Image successfully converted to grayscale...")
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("Process 2 Completed...")

    while flag:
        print("Please select one option: ")
        print("1. Showcase your grayscale image and save it to memory...")
        print("2. Save your grayscale image to memory...")
        op = int(input("Enter your option: "))
        if op==1:
            try:
                print("Opening image...")
                cv2.imshow("Grayscale image", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                print("Image successfully opened...")
                newimage = input("Enter your new converted grayscale file name to save: ")
                print("Saving image...")
                cv2.imwrite(newimage, image)
            except Exception as e:
                print(e)
            finally:
                print("Process 3 Completed...")
                flag = False
        elif op==2:
            try:
                newimage = input("Enter your new converted grayscale file name to save: ")
                print("Saving image...")
                cv2.imwrite(newimage, image)
            except Exception as e:
                print(e)
            finally:
                print("Process 3 Completed...")
                flag = False
        else:
            print("Please select a valid option: ")
            flag = True