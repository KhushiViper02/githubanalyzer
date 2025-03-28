import streamlit as st
from helpers import *
from skills import skills


# Set Page Layout to Wide
st.set_page_config(layout='wide')


# Common Stuff
st.markdown('''

<h1> Github PROFILE README Generator </h1>


''',unsafe_allow_html=True)




sbar = st.sidebar
sbar.markdown('''<a href="https://github.com/KhushiViper02"> Tutorial </a> <br>
<a href = "https://www.linkedin.com/in/khushi-singh-843b50315/"> LinkedIn </a>''' , unsafe_allow_html=True)
page = sbar.radio("Select Page",options=['Home','Generate README'])


if page == 'Home':
    st.subheader("Thank You for using this web app :smile:")
    st.markdown('''
    - Click on 'Generate README' in the sidebar
    - Fill in the text boxes
    - Once you are done, select the 'Generate README' Button
    - If you are happy with the Readme, you can download it
    -)
    ''')
if page == 'Generate README':
    st.subheader("Fill in the text boxes and click on GENERATE README")
    theme_list = ["default","solarized-light","dark", "radical", "merko", "gruvbox", "tokyonight", "onedark", "cobalt", "synthwave", "highcontrast", "dracula"]
    
    github_stats_type = sbar.selectbox(label="Choose Github Stats Card Type",options=['type-1','type-2','type-3'],index=1)
    
    github_stats_theme = ''
    if github_stats_type == 'type-3':
        github_stats_theme = sbar.selectbox(label="Select theme for GitHub Stats",options=theme_list)
    
    isWaka = sbar.checkbox(label= "Include WakaTime Stats",value = True)
    isBlog = sbar.checkbox(label= "Include Blog Posts",value = False)
    isJoke = sbar.checkbox(label= "Include Joke Card",value = True)
    joke_theme = sbar.selectbox(label="Select theme for Joke Card",options=theme_list)
    col1 , col2, col3 = st.columns(3)

    with col1:
        name = st.text_input("Name")
        twitter = st.text_input("Twitter URL")

    with col2:
        github = st.text_input("Github Profile")
        portfolio = st.text_input("Portfolio Link")

    with col3:
        linkedin = st.text_input("Linkedin Profile")
        medium = st.text_input("Medium URL")

    p1_value = '''Github projects, blogs etc...''' 
    p1 = st.text_area("I am currently working on", value=p1_value)

    p2_value = '''Data Science, AWS, Data Engineering etc...'''
    p2 = st.text_area("I am currently learning", value = p2_value)

    p3_value = '''projects, tech articles...'''
    p3 = st.text_area("I am looking to collaborate on", value = p3_value)

    p4_value = '''Python, JavaScript, Freelancing Opportunites, Open Source...'''
    p4 = st.text_area("Let's talk about...",value = p4_value)

    user_skills = st.multiselect("Select Skills",options=skills,default=['python','reactjs','javascript','scikit','c','cpp','sqlite','pytorch','html', 'css', 'java'])
    waka_userid = st.text_input("Wakatime User ID")
    e1 = st.expander("What is Wakatime and how do I get my user ID?")
    with e1:
        st.text('''
                Waktime is an extension for your code editor. 
                It tracks the time you spend coding in a language
                ''')
        st.markdown(''' 
                    - On the top right corner click on your profile icon and click on Settings.
                    - Ensure you have a value in the textbox next to username.
                    - Check the box for the following 'Display photo publicly', 'Display code time publicly ', 'Display languages, editors, os, categories publicly'
                    - In the dropdown next to 'Display code time publicly ', select 'Last 7 days'. If you have a free version, the other options in the dropdown will not work
                    - Click on Save.
            ''')
    st.markdown('<br>' , unsafe_allow_html = True) 
    e2 = st.expander("How to display my latest blog posts?")
    with e2:
        feed_url = st.text_input("URL to your feed")
        st.markdown(f'''
        - Ensure checkbox for blog in sidebar is selected
        - After you update the above feed url, give it a minute and Download the below yml file
        {get_yml(feed_url)}
        ''',unsafe_allow_html = True)
        st.markdown(''' 
        - Create a folder .github.
        - Create a sub-folder called workflows
        - Create a sub-folder and paste the downloaded blog-post-workflow.yml. 
        - Essentially create .github/workflows/blog-post-workflow.yml. If you paste this as the file while creating a new file in Github, it creates the folders for you.
        - In your readme, you blog feed will appear in between the lines 
            ``` 
            <!-- BLOG-POST-LIST:START -->
            <!-- BLOG-POST-LIST:END -->
            ```
        - Once you create the folder and store the file, go to your github repo -> Actions. 
        - Select the workflow in left sidebar and click on run flow. 
        - You will only have to do this once. Github will periodically fetch content from your feed.
        ''')
 

    st.markdown('<br>' , unsafe_allow_html = True) 
    img_url = st.text_input(label='Enter banner image to be added at the top of the README',value = 'https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_1280.jpg')
    c1,c2 = st.columns(2)
    e3 = st.expander("Getting Image URL")
    with e3:
        st.markdown(''' 
    - Enter the URL to the image, ensure URL ends with an extension like '.png','.svg','.gif'
    - If you would like to use a downloaded image, upload the image to your GitHub repo
    - Click on the image file in your repo and click on Open Image in New Tab
    - Copy the URL of image
        ''')
    with c1:
        img_width = st.text_input(label='Enter Image witdh (include units % or px)',value = '100%')
    with c2:
        img_height = st.text_input(label='Enter Image height (include units % or px)',value = '250px')

    e4 = st.expander("Some Image Suggestions")
    with e4:
        fileNames = ["banner1.gif","banner2.jpeg","banner3.gif","banner4.gif","banner5.gif","banner6.gif","banner7.png","banner8.gif","banner9.gif"]
        ih = "250px"
        iw = "100%"
        for banner in fileNames:
            st.markdown(
                f'''
                <img width="{iw}" height = "{ih}" src="https://raw.githubusercontent.com/rahulbanerjee26/githubProfileReadmeGenerator/main/banners/{banner}" alt="cover" />
                <br>
                <br>
                <code> https://raw.githubusercontent.com/rahulbanerjee26/githubProfileReadmeGenerator/main/banners/{banner} </code>
                <br>
                <br>
                <br>
                <br>
                '''
            ,unsafe_allow_html=True)

    save = st.button("Generate README")
    if save:
        code = default_html(name = name, github_username = github, waka_userName= waka_userid,linkedin_url = linkedin,p1 = p1,p2 = p2,p3 = p3,p4 = p4,skills=user_skills,twitter_url=twitter,medium_url = medium, portfolio_url = portfolio,isWaka = isWaka,github_stats_theme = github_stats_theme,isJoke = isJoke, joke_theme = joke_theme,img_url = img_url, img_width= img_width, img_height = img_height, github_stats_type = github_stats_type,isBlog = isBlog)
        st.markdown(download_readme(code),unsafe_allow_html = True)
        st.markdown("---")
        st.markdown(f'''
        ```{code}```
        ''')
        st.markdown("---")
        st.markdown(code, unsafe_allow_html = True)
