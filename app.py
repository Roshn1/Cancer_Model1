import streamlit as st
import joblib
import pandas as pd

model = joblib.load('model.pkl')

st.title('Esophageal Cancer Prediction')

height = st.number_input('Height (cm)', min_value=0, value=170)
weight = st.number_input('Weight (kg)', min_value=0, value=70)
tobacco_smoking_history = st.selectbox('Do you smoke?', ['Yes', 'No'])
age_began_smoking_in_years = st.number_input('Age Began Smoking (Years)', min_value=0, value=0)
stopped_smoking_year = st.number_input('Stopped Smoking Year', min_value=0, value=0)
number_pack_years_smoked = st.number_input('Number of Pack Years Smoked', min_value=0, value=0)
frequency_of_alcohol_consumption = st.number_input('Frequency of Alcohol Consumption', min_value=0, value=0)
amount_of_alcohol_consumption_per_day = st.number_input('Amount of Alcohol Consumed per Day', min_value=0, value=0)
number_of_relatives_diagnosed = st.number_input('Number of Relatives Diagnosed', min_value=0, value=0)

smoking_map = {'Yes': 1, 'No': 0}

input_data = {
   
    'height': height,
    'weight': weight,
    'tobacco_smoking_history': smoking_map[tobacco_smoking_history],
    'age_began_smoking_in_years': age_began_smoking_in_years,
    'stopped_smoking_year': stopped_smoking_year,
    'number_pack_years_smoked': number_pack_years_smoked,
    'frequency_of_alcohol_consumption': frequency_of_alcohol_consumption,
    'amount_of_alcohol_consumption_per_day': amount_of_alcohol_consumption_per_day,
    'number_of_relatives_diagnosed': number_of_relatives_diagnosed,
}

all_features = [
 
  'days_to_death',
 'day_of_form_completion',
 'month_of_form_completion',
 'year_of_form_completion',
 'stage_event_ann_arbor',
 'stage_event_serum_markers',
 'stage_event_igcccg_stage',
 'stage_event_masaoka_stage',
 'primary_pathology_days_to_initial_pathologic_diagnosis',
 'primary_pathology_age_at_initial_pathologic_diagnosis',
 'primary_pathology_year_of_initial_pathologic_diagnosis',
 'primary_pathology_lymph_node_examined_count',
 'primary_pathology_number_of_lymphnodes_positive_by_he',
 'primary_pathology_number_of_lymphnodes_positive_by_ihc',
 'primary_pathology_karnofsky_performance_score',
 'primary_pathology_eastern_cancer_oncology_group',
 'tissue_source_site_IC',
 'tissue_source_site_IG',
 'tissue_source_site_JY',
 'tissue_source_site_KH',
 'tissue_source_site_L5',
 'tissue_source_site_L7',
 'tissue_source_site_LN',
 'tissue_source_site_M9',
 'tissue_source_site_Q9',
 'tissue_source_site_R6',
 'tissue_source_site_RE',
 'tissue_source_site_S8',
 'tissue_source_site_V5',
 'tissue_source_site_VR',
 'tissue_source_site_X8',
 'tissue_source_site_XP',
 'tissue_source_site_Z6',
 'tissue_source_site_ZR',
 'icd_o_3_site_C15.3',
 'icd_o_3_site_C15.4',
 'icd_o_3_site_C15.5',
 'icd_o_3_site_C15.9',
 'icd_o_3_site_C16.0',
 'icd_o_3_histology_8071/3',
 'icd_o_3_histology_8083/3',
 'icd_o_3_histology_8140/3',
 'icd_o_3_histology_8211/3',
 'icd_o_3_histology_8480/3',
 'icd_10_C15.4',
 'icd_10_C15.5',

 'tissue_prospective_collection_indicator_YES',
 'tissue_retrospective_collection_indicator_YES',
 'gender_MALE',
 'race_list_BLACK OR AFRICAN AMERICAN',
 'race_list_WHITE',
 'ethnicity_NOT HISPANIC OR LATINO',
 'other_dx_Yes',
 'vital_status_Dead',
 'alcohol_history_documented_YES',

 'antireflux_treatment_types_Medically TreatedSurgically Treated',
 'antireflux_treatment_types_No Treatment',
 'h_pylori_infection_Never',
 'initial_diagnosis_by_Surveillance',
 'initial_diagnosis_by_Symptomatic',
 'barretts_esophagus_Yes-UK',
 'barretts_esophagus_Yes-USA',
 'goblet_cells_present_YES',
 'history_of_esophageal_cancer_YES',
 'has_new_tumor_events_information_YES',
 'has_follow_ups_information_YES',
 'has_drugs_information_YES',
 'has_radiations_information_YES',
 'stage_event_clinical_stage_Stage IB',
 'stage_event_clinical_stage_Stage II',
 'stage_event_clinical_stage_Stage IIA',
 'stage_event_clinical_stage_Stage IIB',
 'stage_event_clinical_stage_Stage III',
 'stage_event_clinical_stage_Stage IIIA',
 'stage_event_clinical_stage_Stage IIIB',
 'stage_event_clinical_stage_Stage IIIC',
 'stage_event_clinical_stage_Stage IV',
 'stage_event_clinical_stage_Stage IVA',
 'stage_event_clinical_stage_Stage IVB',
 'stage_event_pathologic_stage_Stage IA',
 'stage_event_pathologic_stage_Stage IB',
 'stage_event_pathologic_stage_Stage II',
 'stage_event_pathologic_stage_Stage IIA',
 'stage_event_pathologic_stage_Stage IIB',
 'stage_event_pathologic_stage_Stage III',
 'stage_event_pathologic_stage_Stage IIIA',
 'stage_event_pathologic_stage_Stage IIIB',
 'stage_event_pathologic_stage_Stage IIIC',
 'stage_event_pathologic_stage_Stage IV',
 'stage_event_pathologic_stage_Stage IVA',
 'primary_pathology_histological_type_Esophagus Squamous Cell Carcinoma',
 'primary_pathology_columnar_metaplasia_present_YES',
 'primary_pathology_columnar_mucosa_goblet_cell_present_YES',
 'primary_pathology_columnar_mucosa_dysplasia_Low grade dysplasia',
 'primary_pathology_columnar_mucosa_dysplasia_Negative/no dysplasia',
 'primary_pathology_neoplasm_histologic_grade_G2',
 'primary_pathology_neoplasm_histologic_grade_G3',
 'primary_pathology_neoplasm_histologic_grade_GX',
 'primary_pathology_initial_pathologic_diagnosis_method_Other method, specify:',
 'primary_pathology_initial_pathologic_diagnosis_method_Surgical Resection',
 'primary_pathology_init_pathology_dx_method_other_Esophageal brushing',
 'primary_pathology_init_pathology_dx_method_other_Excisional Biopsy',
 'primary_pathology_init_pathology_dx_method_other_Surgery',
 'primary_pathology_init_pathology_dx_method_other_Surgical Resection',
 'primary_pathology_init_pathology_dx_method_other_Surgical Resection of the Esophagus',
 'primary_pathology_init_pathology_dx_method_other_Surgical resection',
 'primary_pathology_init_pathology_dx_method_other_Tumor Resection',
 'primary_pathology_init_pathology_dx_method_other_cytology',
 'primary_pathology_init_pathology_dx_method_other_surgical resection',
 'primary_pathology_lymph_node_metastasis_radiographic_evidence_YES',
 'primary_pathology_primary_lymph_node_presentation_assessment_YES',
 'primary_pathology_planned_surgery_status_Surgery already performed',
 'primary_pathology_planned_surgery_status_Yes',
 'primary_pathology_treatment_prior_to_surgery_Radiation and Chemotherapy',
 'primary_pathology_residual_tumor_R1',
 'primary_pathology_residual_tumor_R2',
 'primary_pathology_residual_tumor_RX',
 'primary_pathology_radiation_therapy_YES',
 'primary_pathology_postoperative_rx_tx_YES']


for feature in all_features:
    if feature not in input_data:
        input_data[feature] = 0


input_df = pd.DataFrame([input_data])

if st.button('Predict'):
    prediction = model.predict(input_df)

    if prediction == 0:
        st.write("Prediction: No Cancer")
    else:
        st.write("Prediction: Cancer Detected")

        