import streamlit as st
from PIL import Image
import pathlib

import streamlit.components.v1 as components

# set a cool emoji for tab
st.set_page_config(page_title="Othello", page_icon="🎭")

def juxtapose(img1: str, img2: str, height: int = 1000):  # data

    """Create a new timeline component.
    Parameters
    ----------
    height: int or None
        Height of the timeline in px
    Returns
    -------
    static_component: Boolean
        Returns a static component with a timeline
    """

    # load css + js
    cdn_path = "https://cdn.knightlab.com/libs/juxtapose/latest"
    css_block = f'<link rel="stylesheet" href="{cdn_path}/css/juxtapose.css">'
    js_block = f'<script src="{cdn_path}/js/juxtapose.min.js"></script>'

    # write html block
    htmlcode = (
        css_block
        + """ 
    """
        + js_block
        + """
        <div id="foo" style="width: 95%; height: """
        + str(height)
        + '''px; margin: 1px;"></div>
        <script>
        slider = new juxtapose.JXSlider('#foo',
            [
                {
                    src: "'''
        + img1
        + '''",
                    label: 'img1',
                },
                {
                    src: "'''
        + img2
        + """",
                    label: 'img2',
                }
            ],
            {
                animate: true,
                showLabels: true,
                showCredits: true,
                startingPosition: "50%",
                makeResponsive: true
            });
        </script>
    """
    )
    static_component = components.html(
        htmlcode,
        height=height,
    )
    return static_component

STREAMLIT_STATIC_PATH = (
    pathlib.Path(st.__path__[0]) / "static"
)  # at venv/lib/python3.9/site-packages/streamlit/static

Cubist = Image.open(r"Cubist.jpg")
Othello = Image.open(r"othello.jpg").rotate(90)
width, height = Othello.size

# Define the coordinates for cropping
left = 0
upper = 600
right = width
lower = height - 600

# Crop the image
Othello = Othello.crop((left, upper, right, lower))

IMG1 = "othello.jpg"
IMG2 = "Cubist.jpg"



#############
# Title
st.title("Behind the Lies and the Truths of Othello: The Green-Eyed Monster")
st.caption("By: Maya, Sarah, and Ryan")
st.divider()
st.write(
"""
	In our Othello project, we rendered our perception of Othello in a cubist form. Starting from Maya’s creation of a Spanish-esque melody, we decided on creating a cubist drawing that appears fragmented and abstracted, much like characteristics of the Cubist art movement. Correspondingly, our artwork embraces elements that symbolizes the motif of lies/truth and gender roles within Othello. 

The fragmented mirrors express the distinct perspectives Iago conforms to, based on his audience. These geometric shapes represent walls closing in on Desdemona, making it seem like she is claustrophobic. The eye symbolizes the green-eyed monster (Iago) while the arm kills Desdemona on the right. As his large hand is directly coming out from his chest, it delineates how his hatred towards Desdemona comes from his heart and overpowers Desdemona. This could possibly attest to the patriarchal power structure rooted within Othello and possibly of how jealous he is of Desdemona’s purity. As well, it reveals the way Iago dictates Othello’s jealousy and hatred towards Desdemona, controlling his emotions through his lies. Additionally, Desdemona was inspired by the painting The Scream by Edvard Munch which builds a very anxious and disturbed ambience. We chose to interpret Othello in a Cubist way since Othello is a play set in a war period, just as the Cubist art movement was a response to the war, evoking a serious and violent sentimentality. 

"""
)

st.audio("project_song.mp3", format="audio/mpeg")
st.divider()

##################
# Displaying Images

# Create a select box for the tabs
option = st.selectbox(
    'Veiwing Options',
    ('Slider', 'Images'), help="Select a tab to choose how to view the images")

# Show the images tab
if option == 'Images':
    st.image(Othello)

    with st.expander("Learn More about Cubism"):
        st.image(Cubist)
        st.caption("Guernica, by Pablo Picasso (1937), oil on canvas. Museo Reina Sofía de Madrid, Spain.")
        st.write("""
            Cubism began in the early twentieth century by artist Pablo Picasso. To emphasize the two-dimensionality of nature in rejection of the way art had copied nature up until then, artists of this movement would reduce objects to its most basic form and compose geometric shapes and linear structures based on a 2-D perspective. Artists would analyze and dissect certain objects in multiple perspectives and accordingly draw each of them. To the viewer, cubist artworks are usually indiscernible because of how abstract and intricately layered they are. Yet, it gives the audience a true, even multidimensional perspective within a two dimensional plane. 
        """)

if option == 'Slider':

    Cubist.resize((Othello.size))
    Othello.save(STREAMLIT_STATIC_PATH / IMG1)
    Cubist.save(STREAMLIT_STATIC_PATH / IMG2)

    juxtapose(IMG1, IMG2)
