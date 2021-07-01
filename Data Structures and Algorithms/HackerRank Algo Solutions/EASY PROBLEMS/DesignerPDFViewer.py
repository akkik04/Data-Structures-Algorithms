# DESIGNER PDF VIEWER HACKERRANK SOLUTION:

# creating a function to calculate the area of the highlighted region in the PDF.
def designerPdfViewer(h, word):

    # creating a variable to store the value for the height of the highlighted area.
    height = 0

    # creating a variable to store the length of the word.
    x = len(word)

    # creating a for-loop to iterate for the word.
    for i in word:

        # code to find the max height of the word using the ascii values of the characters.
        height = max(height, h[ord(i) - ord('a')])
    
    # code to calculate the area of the highlighted region.
    area = height * x
    
    # returning the area of the highlighted region.
    return area

# receiving input.
h = list(map(int, input().rstrip().split()))
word = input()

# code to print the final output, which indicates the area of the highlighted region in the PDF.
result = designerPdfViewer(h, word)
print(result)