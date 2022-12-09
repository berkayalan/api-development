import packages.data_processor as dp
import streamlit as st 
import joblib

# Load the model
diabetes_clf = joblib.load(open('./models/diabetes_detector_model.pkl','rb'))

### MAIN FUNCTION ###
def main(title = "Awesome Streamlit Diabetes classification App".upper()):
    st.markdown("<h1 style='text-align: center; font-size: 65px; color: #4682B4;'>{}</h1>".format(title), 
    unsafe_allow_html=True)
    st.image("./images/diabetes.jpeg")
    info = ''
    
    with st.expander("1. Check if yo've diabetes or not'"):

        pregnancy = st.number_input("Please enter your Pregnancies")
        glucose   = st.number_input("Please enter your Glucose")
        blood     = st.number_input("Please enter your BloodPressure")
        skin      = st.number_input("Please enter your SkinThickness")
        insulin   = st.number_input("Please enter your Insulin")
        bmi       = st.number_input("Please enter your BMI")
        pedigree  = st.number_input("Please enter your Diabetes Pedigree Function")
        age       = st.number_input("Please enter your Age")

        inputs = [pregnancy,glucose,blood,skin,insulin,float(bmi), float(pedigree),age]

        print(inputs)

        if st.button("Predict"):

            prediction = diabetes_clf.predict([inputs])

            if(prediction[0] == 0):
                info = 'You don\'t have diabetes!'

            else:
                info = 'Unfortunately you have diabetes!'
            st.success('Prediction: {}'.format(info))

if __name__ == "__main__":
    main()