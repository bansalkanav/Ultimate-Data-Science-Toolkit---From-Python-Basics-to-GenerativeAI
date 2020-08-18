import streamlit as st

step_2_text = ["Go to aws.amazon.com and click on 'Create an AWS Account'", "Enter 'email', 'pasword' and 'AWS account name'", "Enter all the required details and click on 'Create Account and Continue'", "Enter Credit/Debit card details", "Make Payment", "Confirm your identity (Mobile Number)", "Select a Basic Plan (Free)", "Wait for activation email - It may take 24 hours to arrive", "This is account creation email (Not an activation email)", "Go to console.aws.amazon.com and login with your credentials", "Click on 'Home' to open AWS Management Console", "Click on 'Launch a virtual machine (with EC2)'", "If your account is not active, you will see this screen", "This is your Account Activation Email"]
step_3_text = ["Goto aws.amazon.com and 'Sign in to the Console'", "Click on 'Launch a Virtual Machine(with EC2)'","Choose an OS (Recommended - UBUNTU Server Free Tier)", "Choose t2.micro Instance and click 'Review and Launch'", "Click 'Launch'", "Create a new key pair", "Download the Key Pair and Launch the Instance", "Click on 'View Instance'", "You might see Instance State as 'Pending'", "Go to 'Security Groups' and 'Create security group'", "Enter Basic Details and add 'Inbound rules' and click on 'Create security group'", "Go to 'Network Interfaces' and right click on the available interface and click 'Change Security Groups'", "Add 'anywhere' and click 'Save'", "Go to 'Instances' and wait for 'running' Instance State. Right Click and 'Connect'", "Copy this ssh command to connect to your Instace from localhost"]
step_4_text = ["'web_app' contains my application and '.pem' is the private key", "Use this SSH command to connect with AWS remote instance", "Upgrade your Linux Box", "Install pip3 and all other required libraries", "Install 'tmux'", "Logout and Upload the 'web_app' folder from localhost to AWS remote instance", "Now connect to AWS remote instance again using SSH and create a tmux instance", "You are now in tmux instance (Observe the green bar on the bottom of screen)", "Go to 'web_app' directory and run the application", "Open External URL in your browser", "Press 'ctrl+b d' to exit tmux instance (It will still be running in background)", "Connect again to remote instance and enter the tmux instance", "tmux instance is running even after logout from SSH", "Web App is also running at External URL"]

st.sidebar.subheader("Deployment on AWS")
st.sidebar.info("Complete Documentation")
st.sidebar.success("This is a complete step by step documentation to deploy your streamlit application")
st.sidebar.warning("Made with extra :heart: :heart: :sunglasses:")

st.title("Deployment on AWS")


st.header("Step - 1 : Create a web application on your computer")
st.image("img/aws0a.PNG", use_column_width=True)

st.header("Step - 2 : Create AWS Account")
if(st.checkbox("Explore Step - 2")):
    step_2 = st.number_input("Sub Steps - (1 to 14)", 1, 14)
    step_2_loc = "img/aws"+str(step_2)+".PNG"
    st.subheader(step_2_text[step_2-1])
    st.image(step_2_loc, use_column_width=True)

st.header("Step - 3 : Create AWS EC2 instance")
st.image("img/aws0b.PNG", use_column_width=True)
if(st.checkbox("Explore Step - 3")):
    step_3 = st.number_input("Sub Steps - (15 to 29)", 15, 29)
    step_3_loc = "img/aws"+str(step_3)+".PNG"
    st.subheader(step_3_text[step_3-15])
    st.image(step_3_loc, use_column_width=True)

st.header("Step - 4 : Hosting the web app on AWS")
st.image("img/aws0c.PNG", use_column_width=True)
if(st.checkbox("Explore Step - 4")):
    step_4 = st.number_input("Sub Steps - (30 to 43)", 30, 43)
    step_4_loc = "img/aws"+str(step_4)+".PNG"
    st.subheader(step_4_text[step_4-30])
    st.image(step_4_loc, use_column_width=True)
