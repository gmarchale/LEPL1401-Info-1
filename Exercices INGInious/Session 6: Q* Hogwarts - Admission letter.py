# Voir ce lien : https://github.com/rverschuren/Info/blob/master/Exercices/6/Q%20Hogwarts%20-%20Admission%20letter.py
# -------------------------------------------
#   Solution par ( @rverschuren ) 
# -------------------------------------------
def write(letter_template, name):
    try: 
        with open(letter_template, 'r') as f:
            template = f.read()
        template = template.split('#')
        output = name.join(template)
        
        with open(letter_template, 'w') as f:
            f.write(output)
            
    except Exception as exc:
        raise OSError("une erreur s'est produite") from exc
