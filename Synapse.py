import streamlit as st
import synapseclient
from synapseclient import Project, Folder, File
st.title("Synapse")
db_token = st.secrets["DB_TOKEN"]
syn = synapseclient.login(authToken=db_token)
profile = syn.getUserProfile()

project_name = 'MySynapseStreamlitOne'
project = Project(project_name)
project = syn.store(project)
st.success(project)
entity = syn.get(project_name)
st.success(entity)
