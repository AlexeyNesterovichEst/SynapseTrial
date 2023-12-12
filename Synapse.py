import streamlit as st
import synapseclient
st.title("Synapse")
db_token = st.secrets["DB_TOKEN"]
syn = synapseclient.login(authToken=db_token)
profile = syn.getUserProfile()

project_name = 'MySynapseStreamlit'
project = Project(project_name)
project = syn.store(project)
entity = syn.get(project_name)
st.success(entity)
