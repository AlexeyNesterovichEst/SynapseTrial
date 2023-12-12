import streamlit as st
import synapseclient
from synapseclient import Project, Folder, File
st.title("Synapse")
db_token = st.secrets["DB_TOKEN"]
syn = synapseclient.login(authToken=db_token)
profile = syn.getUserProfile()

if "project_id" not in st.session_state:
  st.session_state.project_id = ""

project_name = 'MySynapseStreamlitTwo'
project = Project(project_name)
project = syn.store(project)
st.success(type(project.id))
st.session_state.project_id = project_id
st.success(st.session_state.project_id )
entity = syn.get(st.session_state.project_id)
st.success(entity)
