# Unix script for rendering all of the videos for me.
# If you are having problems running this follow the following steps
# 1) If using windows, wipe your computer and install linux (or buy a mac)
# 2) Install manim: https://docs.manim.community/en/stable/installation.html
# 3) chmod +x render.sh
# 4) ./render.sh

current_file=''

function def_file {
    current_file="$1.py"
    echo "Switching to $current_file"
}

function render {
    scene=$1
    echo "Rendering $current_file - $scene"
    manim -qk --save_sections $current_file $scene
}

function main {
    def_file "text"
    render "IntroduceSensors"
    render "ResistanceEquation"
    render "ResistanceTable"
    render "RainGaugeText"
    render "WindSensorText"
    render "WindDirectionSensorText"
    render "ADCText"
    render "FixedResitorText"
    render "StevenScreenCopyright"
    render "ImageNotFound"
    render "PullDownNote"
    render "MicroclimateDefinition"
    render "TranscriptSources"
}

time main
