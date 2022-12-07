**DISCLAIMER:** All patient data has been previously de-identified. Multiple endpoints require authentication to create, update or delete records. Further authentication will be required once the API functionality is extended in order to follow [HIPAA specifications.](https://www.hhs.gov/hipaa/for-professionals/security/index.html)

## Read Patient Records

The API supports POST methods for reading Patient records via JSON. The basic Patient data includes weight, height, age, etc (more on the Swagger Docs specification below).

Patient data is also related to other Medical data, like Cardiac Diagnosis and Surgical Procedures, as well as other data like State, Municipality, etc.


## Read Medical Terms Data

The API provides access to POST and GET methods for retrieving lists of medical terms associated with the Patient data, which are stored separately from the Patient records as they may contain labels and information not related to the Patient as well as many-to-one relationships with the Patient. 

## ML Prediction

### Valid Diagnosis: 
    
- "CIA"
- "CIV"
- "Estenosis"
- "PCA"
- "Other_Diagnosis"
- "Coartacion Aortica"
- "Tetralogia de Fallot"
- "Atresia"
- "Post-Surgical Procedure"
- "Hipoplasia"


### Valid Surgical Procedures.

- "Parche comunicacion interauricular CIA"
- "Vena cava inferior parche"
- "Other_Procedure"
- "Cierre de Conducto Arterioso"
- "Reparacion de Canal AV"
- "Reparacion de Tetralogia de Fallot"
- "Procedimiento de Glenn"
- "Reparacion de arco aortico"
- "Fistula sistemico pulmonar"
- "Procedimiento de Fontan"


## Copyright

2022, Daniela Soto, Galo Cazares, Alberto Valdez