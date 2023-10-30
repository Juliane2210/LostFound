
import sys
import os

# add backend subfolder to expose the ImageService
root_folder = os.path.abspath(os.path.dirname(__file__))
sys.path.append(root_folder+"\\..\\backend")
import imageservice 


m_imageService = imageservice.ImageService()


def report_item():
    item_type = input("Is the item 'lost' or 'found' ?")
    description = input("Enter item description: ")
    location = input("Enter the location: ")

    item = {
        'type':item_type,
        'description': description,
        'location': location
    }

    database.append(item)
    save_to_file(database)
    print("Item reported successfully!")

def search_items():
    #choose from a list of keywords...from a file and show it to the user...
    keyword = input("Enter a keyword to search for: ")


    found_items = m_imageService.matchCategory(keyword)


    # implement printing put of the found items.
  

    if found_items:
        print("Found items:")
        for item in found_items:
            print(f"Type: {item['type']}, Description: {item['description']}, Location: {item['location']}")

    else:
        print("No matching items found.")




def main():   

    while True:
        print("\nLost and Found System")
        print("1. Report a Lost or Found Item")
        print("2. Search for Lost or Found Items")
        print("3. Exit")

        choice= input("Enter your choice: ")

        if choice =="1":
            report_item()
        elif choice == "2":
            search_items()
        elif choice == "3":
            print("Exiting the Lost and Found System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ =="__main__":
    main()





# import cv2
# import numpy as np

# # Sample data (replace with your own dataset)
# lost_items = [
#     {"description": "Lost keys", "image_path": "lost_keys.jpg"},
#     {"description": "Lost wallet", "image_path": "lost_wallet.jpg"},
# ]

# found_items = [
#     {"image_path": "found_item.jpg"},
# ]

# def preprocess_image(image_path):
#     # Load and preprocess the image
#     image = cv2.imread(image_path)
#     # Apply any necessary image preprocessing steps, e.g., resizing, color adjustments

#     return image

# def compare_images(image1, image2):
#     # Compare two images using image processing techniques
#     # Implement image similarity or feature matching algorithms

#     # Example: Calculate mean squared error (MSE) as a simple similarity metric
#     mse = np.mean((image1 - image2) ** 2)
#     return mse

# def find_matches(found_image, lost_items):
#     matches = []

#     # Preprocess the found image
#     found_image = preprocess_image(found_image)

#     for lost_item in lost_items:
#         # Preprocess the lost item image
#         lost_image = preprocess_image(lost_item["image_path"])
        
#         # Compare the found item with the lost item
#         similarity = compare_images(found_image, lost_image)

#         # Set a similarity threshold for a match
#         if similarity < 1000:  # Adjust this threshold as needed
#             matches.append((lost_item["description"], similarity))

#     return matches

# def main():
#     print("Welcome to the Lost and Found System")
#     found_item_image_path = input("Please enter the path to the found item image: ")
#     matches = find_matches(found_item_image_path, lost_items)

#     if matches:
#         print("Potential matches found:")
#         for description, similarity in matches:
#             print(f"- Description: {description}, Similarity: {similarity:.2f}")
#     else:
#         print("No matches found.")

# if __name__ == "__main__":
#     main()




