import image
class ImageService:
    def __init__(self):
        self.foundImageDictionary = none

    # GET

    def matchCategory(self, category: str, originalImage: str = None) -> object:
        """
        This function will match the image of the lost object with the category 
        of the lost object with our database of found images under that category

        """
        print("The closest matching image for", category)
        return {}

    def matchDateTime(self, date, location) -> object:
        """
        This function is the same as above, but with different parameters
        """
        foundImage = image.Image("path")
#finish this fct using yeshvendra's code

        return foundImage

# PUT

    def registerImage():
        """ 
        """
        return {}
# DELETE

    def deleteImage():
        print("deleted")
