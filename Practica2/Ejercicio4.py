def main():
 
    archivo = input("Nombre del archivo: ").strip().lower()

   
    if archivo.endswith(".gif"):
        print("image/gif")
    elif archivo.endswith(".jpg") or archivo.endswith(".jpeg"):
        print("image/jpeg")
    elif archivo.endswith(".png"):
        print("image/png")
    elif archivo.endswith(".pdf"):
        print("application/pdf")
    elif archivo.endswith(".txt"):
        print("text/plain")
    elif archivo.endswith(".zip"):
        print("application/zip")
    else:
        
        print("application/octet-stream")

main()