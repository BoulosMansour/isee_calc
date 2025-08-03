import streamlit as st
import json

# Load configuration
with open('config.json', 'r') as f:
    config = json.load(f)

st.title('Calculate your ISEE')

people_count = st.slider("Number of people in the household", 1, 10, 1, format="%d")
se = config['SE'][str(people_count)]
mainResidence = st.number_input("Main residence area (in square meters)")
otherBuildings_count = st.slider("Number of other buildings owned", 0, 10, 0, format="%d")
otherBuildings_area = dict()
for i in range(otherBuildings_count):
    area = st.number_input(f"Area of other building {i+1} (in square meters)", key=f"other_building_{i}")
    otherBuildings_area[i] = area
bankStatement = st.number_input("Bank statement amount (in LBP)") / config['rate']
income = st.number_input("Annual income (in LBP)") / config['rate']
rent = st.number_input("Annual rent (in LBP)") / config['rate']


# Calculating ISEE
realState = 2/3*((mainResidence*500)-52500) + sum(float(area) for area in otherBuildings_area.values()) * 500
if realState < 0:
    realState = 0
movableAssets = bankStatement - 6000
if movableAssets < 0:
    movableAssets = 0
if rent > 7000:
    rent = 7000
isr = income - rent
isp = realState + movableAssets
ise = 0.2*isp + isr
ispe = isp/se
isee = ise/se

# display results
st.subheader("Results")
st.write(f"ISEE: {isee:.2f} €")
st.write(f"ISPE: {ispe:.2f} €")
fullScholarship = ispe < config["ispe_threashold"] and isee < config["isee_threshold"]
st.write(f"Full scholarship eligibility: {'Yes' if fullScholarship else 'No'}")