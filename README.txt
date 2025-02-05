Το παρόν project είναι μια containerized εφαρμογή web scraping γραμμένη σε Python, η οποία είναι hosted στο Azure Kubernetes Service (AKS).

Η εφαρμογή κάνει scrape δεδομένων βιβλίων από το Books to Scrape και φιλτράρει τα αποτελέσματα με βάση τα κριτήρια που ορίζει ο χρήστης:

-Κατηγορία βιβλίου
-Ελάχιστη τιμή
-Μέγιστη τιμή

Η εφαρμογή επιστρέφει:

-Τίτλους βιβλίων που ανταποκρίνονται στα κριτήρια
-Τιμές των βιβλίων
-Star Rating
-Διαθεσιμότητα (In Stock ή Out of Stock)

Για το containerization της εφαρμογής χρησιμοποιήθηκε το Docker.Το Docker image ανέβηκε στο Docker Hub.Το AKS Cluster χρησιμοποίησε αυτό το image για να δημιουργήσει το Kubernetes cluster όπου τρέχει η εφαρμογή.

Η εφαρμογή έτρεξε χωρίς πρόβλημα από το AKS Cluster που δημιουργήθηκε. Υπάρχει φάκελος στο repository με τα ανάλογα screenshots . 




This project is a containerized web scraping application written in Python, which is hosted on Azure Kubernetes Service (AKS).

The application scrapes book data from Books to Scrape and filters the results based on criteria defined by the user:

-Book Category
-Minimum Price
-Maximum Price

The application returns:

-Book Titles that match the criteria
-Book Prices
-Star Rating
-Availability (In Stock or Out of Stock)
For the containerization of the application, Docker was used.
The Docker image was uploaded to Docker Hub, and the AKS Cluster used this image to create the Kubernetes cluster where the application runs.

The application ran successfully from the AKS Cluster that was created.
There is a folder in the repository containing the corresponding screenshots. 