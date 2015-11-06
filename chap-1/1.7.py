# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_img(img, N):
    for layer in range(N/2):
        for i in range(layer, N-layer-1):
            tmp                         = img[i][N-layer-1]
            img[i][N-layer-1]           = img[layer][i]
            img[layer][i]               = img[N-layer-i-1][layer]
            img[N-layer-i-1][layer]     = img[N-layer-1][N-layer-i-1]
            img[N-layer-1][N-layer-i-1] = tmp
    for i in range(N):
        print(img[i])

def rotate_img(img, N):
    for layer in range(N/2):
        for i in range(layer, N-layer-1):
            tmp                         = img[layer][i]
            img[layer][i]               = img[N-i-1][layer]
            img[N-i-1][layer]     = img[N-layer-1][N-i-1]
            img[N-layer-1][N-i-1] = img[i][N-layer-1]
            img[i][N-layer-1]           = tmp
    for i in range(N):
        print(img[i])


if __name__ == "__main__":
    img = [[1 ,2 ,3 ,4 ],
           [5 ,6 ,7 ,8 ],
           [9 ,10,11,12],
           [13,14,15,16]]
    rotate_img(img, len(img))