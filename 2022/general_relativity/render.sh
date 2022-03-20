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
    mkdir -p "dist/$current_file"
}

function render {
    scene=$1
    echo "Rendering $current_file - $scene"
    manim -qk $current_file $scene
}

function main {
    def_file "3d"
    render "ThreeDimensionsPlusTime"

    def_file "box"
    render "FloatingBox"

    def_file "falling_ball"
    render "TwoObjectsFalling"

    def_file "grav_grid"
    render "GravityGrid"

    def_file "jump"
    render "CircleJump"

    def_file "stars"
    render "StarBackground"

    def_file "text"
    render "WaterbottleQuestion"
    render "EquivalencePrinciple"
    render "BasicGravityFormula"
    render "Conclusions"
    render "Placeholder"
    render "Gravity"
    render "Endscreen"

    def_file "components"
    render "DrawArrow"
    render "DrawShuttleDashed"
    render "DrawShuttleSolid"
    render "BasicDrawArrow"

    def_file "citations"
    render "CitationIntro"
    for i in {1..7}; do
        render "Citation$i"
    done
}

time main
