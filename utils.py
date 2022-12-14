import cv2

def put_drawings(img, is_mask, face_loc):
    
    x, y, w, h = face_loc
    
    # draw rectangles around faces
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0) if is_mask==1 else (0,0,255), 1)
    # decorate the corners
    # 0
    cv2.line(img, (x, y-30), (x, y-10), (0, 255, 0) if is_mask==1 else (0,0,255), 4)
    cv2.line(img, (x, y-30), (x+20, y-30), (0, 255, 0) if is_mask==1 else (0,0,255), 4)
    # 1
    cv2.line(img, (x+w, y-30), (x+w-20, y-30), (0, 255, 0) if is_mask==1 else (0,0,255), 4)
    cv2.line(img, (x+w, y-30), (x+w, y-10), (0, 255, 0) if is_mask==1 else (0,0,255), 4)
    # 2
    cv2.line(img, (x+w, y+h), (x+w, y+h-20), (0, 255, 0) if is_mask==1 else (0,0,255), 4)
    cv2.line(img, (x+w, y+h), (x+w-20, y+h), (0, 255, 0) if is_mask==1 else (0,0,255), 4)
    # 3
    cv2.line(img, (x, y+h), (x+20, y+h), (0, 255, 0) if is_mask==1 else (0,0,255), 4)
    cv2.line(img, (x, y+h), (x, y+h-20), (0, 255, 0) if is_mask==1 else (0,0,255), 4)
    
    # draw a rectangle to put the result inside
    cv2.rectangle(img, (x, y-30), (x+w, y), (0, 255, 0) if is_mask==1 else (0,0,255), 1)
    
    return img

def display_result(img, is_mask, face_loc):
    
    x, y, w, h = face_loc
    
    img = put_drawings(img, is_mask, face_loc)
    # put the result 
    cv2.putText(img, 'Mask' if is_mask==1 else 'No mask' , (x+20, y-8), 0, .8, (0, 255, 0) if is_mask==1 else (0,0,255), 2)
    return img

