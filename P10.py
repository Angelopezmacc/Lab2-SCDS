# Import of RegEx library
import re

# Function that prevents XSS and SQLi
def no_XSS_or_SQLi (text):
    
    notAllowed = ["<script>","'","</script>","<",">",] #List of banned words
    coincidences = 0
    
    for i in range(len(notAllowed)):
        
        validate = re.findall(notAllowed[i], text)
        if len(validate) >= 1:
            coincidences += 1
        
    if coincidences >= 1:
        print("lA ENTRADA NO ES VÁLIDA. VUELVA A INTENARLO")
        
    if coincidences == 0:
        print("Entrada correcta.")

no_XSS_or_SQLi("<script> alert('document.cookie') </script>")
no_XSS_or_SQLi("'")



