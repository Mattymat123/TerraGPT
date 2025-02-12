footer = """<style>
a:link , a:visited{
    color: blue;
    background-color: transparent;
    text-decoration: underline;
}

a:hover,  a:active {
    color: red;
    background-color: transparent;
    text-decoration: underline;
}

.footer {
    position: fixed;
    left: 125px; /* Changed from 125px to 0 to ensure it spans the full width */
    bottom: 0;
    font-size:32px;
    width: 100%;
    background-color: transparent;
    color: black;
    text-align: center;
    z-index: 1000; /* Ensure the footer stays on top */
}
</style>
<div class="footer">
    <p>
        <span style="background: linear-gradient(to right, #081f26, #0b2b35); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 32px !important;">©2025 Machintu</span>
    </p>
</div>"""