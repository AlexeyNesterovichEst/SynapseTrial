import streamlit as st
st.title("Synapse")
token = "eyJ0eXAiOiJKV1QiLCJraWQiOiJXN05OOldMSlQ6SjVSSzpMN1RMOlQ3TDc6M1ZYNjpKRU9VOjY0NFI6VTNJWDo1S1oyOjdaQ0s6RlBUSCIsImFsZyI6IlJTMjU2In0.eyJhY2Nlc3MiOnsic2NvcGUiOlsidmlldyIsImRvd25sb2FkIiwibW9kaWZ5Il0sIm9pZGNfY2xhaW1zIjp7fX0sInRva2VuX3R5cGUiOiJQRVJTT05BTF9BQ0NFU1NfVE9LRU4iLCJpc3MiOiJodHRwczovL3JlcG8tcHJvZC5wcm9kLnNhZ2ViYXNlLm9yZy9hdXRoL3YxIiwiYXVkIjoiMCIsIm5iZiI6MTcwMjM3MDI2MCwiaWF0IjoxNzAyMzcwMjYwLCJqdGkiOiI0NTU1Iiwic3ViIjoiMzQ4ODYzMyJ9.PzKeT1sbxuOdo4rY_afNMOb31W2GWrLN0EgxUFOxotDDDWnNKY-tYjlFAyRNRT6Ks-MABvUgvMvp2vN6UJ-ewiwPodxoMvAsgC_5VkCR1vfWnj73ZESifVqYdvZAszkz3GuWZ-AXsCcV51XuBu0tWwjUvDTgmPFYB6B-QAZRaUnQ6tIJhdkfuvyvRneykb-XGBMPhad1qQ57o_BEmKlFPz2ja7emINSXyt1cqgaM42oJYOQjl14UPcp4uVRDh7JGYfc7A_TKZ3UPdA91A-2aqejjsGEJnf9yxYBuQtLk5ZdlK49HY3k-hHCBp5k2a7esQWjJtTL_grjVrCTDEhaJ3Q"

import synapseclient
syn = synapseclient.login(authToken=token)
