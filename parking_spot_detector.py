import numpy as np 
import cv2
from imutils.perspective import four_point_transform



color = (255,255,0)
counter , counter2,  counter3 , counter4 = 0,0 , 0 , 0
four_counter = 0
white = 0
flag = 1
first_pos = 0
flag2 = 1
pos_list = []
big_list = []
bigger_list = []
all_pos = []
another = []
white_list = []
car_number = 3
# warped = 0
def click_position(event , x , y , flag , param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global first_pos , another
        global counter , counter2 , flag2
        pos_list.append((x , y))
        another.append(pos_list[-1])
        # if flag2:
        # big_list.append(pos_list[counter2])
        # #     flag2 = 0    
        # # big_list[0] = pos_list[0]
        # bigger_list.append(big_list.copy())
        # big_list.clear()
        print(" another list is : ")
        print(another)
        print("pos list : ")
        print(pos_list)
        # print("the bigger list : ")
        # print(bigger_list)
        # print("the big list is :")
        # print(big_list)
        # if flag :
        #     first_pos = pos_list[0]
        #     x , y = first_pos[0] , first_pos[1]
        #     print("first pos : " +str(first_pos[0]) + str(first_pos[1]))
        #     flag = 0
        counter +=1
        counter2 += 1


image = cv2.imread(r"C:\Users\Morvarid\Desktop\python\open_cv\opencv_practice\stthomas-parking-transportation-lot.jpg")
image1 = image.copy()
overlay = image1.copy()


img_gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray , (5 , 5) , 0)
img_threshold = cv2.adaptiveThreshold(img_blur , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY_INV  , 25 , 16)
img_median = cv2.medianBlur(img_threshold , 5)
kernel = np.ones((3,3) , np.uint8)
img_dialate = cv2.dilate(img_median , kernel , iterations=1)


while cv2.waitKey(1) != ord("q"):
    # global doc_cnts
    # overlay = cv2.imread(r"C:\Users\Morvarid\Desktop\python\open_cv\opencv_practice\stthomas-parking-transportation-lot.jpg")

    global warped

    if len(pos_list)==2:

        if flag :

            first_pos = pos_list[0]
            print(pos_list[0])
            print(first_pos)
            flag = 0

        first_point = (pos_list[0][0] , pos_list[0][1])
        second_point = pos_list[1]
        cv2.line(image , first_point , second_point , color , 3)
        pos_list.pop(0)
        # counter2 = 1
        # print(pos_list)

        if counter == 4:
            # print(first_pos)
            four_counter += 1
            all_pos.append(another)
            print("all_pose continas : " + str(all_pos))


            # print("makig the wanted line for you")
            cv2.line(image , pos_list[0] , first_pos , color , 3)
            pos_list.clear()
            flag = 1
            counter = 0
            file = open("positions.txt" , "a")
            file.write(str(another)+"\n")
            file.close()
            print("before np.array : " +str(another))
            another = np.array(another)
            print("another is : " + str(another))
            doc_cnts = another
            print("doc_cnts : " + str(doc_cnts) +" and the length of it is : " + str(len(doc_cnts)))
            warped = four_point_transform(img_dialate, doc_cnts.reshape(4, 2))
            big_list.append(warped)
            # print("another is : " + str(another))
            

            another = list(another)
            # file = open("positions.txt" , "a")
            # file.write(str(doc_cnts)+"\n")
            # file.close()
            #also send it to the file that we have
            another.clear()
            # del another
            cv2.resize(warped ,(0,0) ,  fx=0.5 , fy=0.5)
            # cv2.imshow("wapred " , warped)
    # if len(big_list)==3:
        # for frame in big_list:
            
            # cv2.imshow(str(counter2) , warped)
            if(four_counter== car_number):
                # image = image.copy()
                for car in big_list:
                    # cv2.imshow(str(car) , car)
                    print("the big list contains " + str(len(big_list)))
                    white = cv2.countNonZero(car)
                    white_list.append(white)
                    print(str(big_list[counter4])+ str(white))
                    if white < 1000 :
                        cv2.circle(image , all_pos[counter4][0] , 1 , (0,255,0) , -1)
                        cv2.putText(image , str(white), all_pos[counter4][0] , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (255,255,0) , 1 )
                        # cv2.fillConvexPoly(image , all_pos[counter4] , (0,255,0))
                        # points = np.array([all_pos[counter4][0] , all_pos[counter4][0]])
                        # overlay = cv2.imread(str(car))
                        # overlay = cv2.imread(r"C:\Users\Morvarid\Desktop\python\open_cv\opencv_practice\stthomas-parking-transportation-lot.jpg")
                        overlay = image.copy()


                        cv2.fillPoly(overlay , np.int32([all_pos[counter4]]) , (0,255,0))
                        alpha = 0.4
                        image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
                        counter4 += 1
                    else:
                        # if counter4 ==1:
                        #     overlay = cv2.imread(r"C:\Users\Morvarid\Desktop\python\open_cv\opencv_practice\stthomas-parking-transportation-lot.jpg")
                        #     cv2.fillPoly(overlay , np.int32([all_pos[counter4]]) , (0,0,255))
                        #     alpha = 0.6
                        #     image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
                            
                        # print("couldn't get to the if statement ")
                        cv2.putText(image , str(white), all_pos[counter4][0] , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0,0,255) , 1 )
                        # overlay = cv2.imread(r"C:\Users\Morvarid\Desktop\python\open_cv\opencv_practice\stthomas-parking-transportation-lot.jpg")
                        overlay = image.copy()
                        cv2.fillPoly(overlay , np.int32([all_pos[counter4]]) , (0,0,255))
                        alpha = 0.3
                        image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
                        # del overlay


                        counter4 +=1 
            print(white_list)
                        

        # counter3 += 1

    
    
            
    # if four_counter != 4:
    cv2.imshow("the image "  , image)
    # else:
    #     # cv2.destroyAllWindows()
    #     cv2.imshow("the second image " , image1)
    cv2.setMouseCallback("the image " , click_position)


    # saba certificated

