<div>
    <span class="a" />
    <span class="b" />
    <span class="a" />
    <span class="b" />
</div>

<style>
    @keyframes animation {
        0% {
            height: 20px;
        }
        50% {
            height: 100px;
        }
        100% {
            height: 20px;
        }
    }

    div {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;

        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    span {
        width: 20px;
        height: 100px;

        background-color: white;

        border-radius: 20px;

        margin-left: 5px;
        margin-right: 5px;
    }

    .a {
        animation: animation 1s infinite;
    }

    .b {
        animation: animation 2s infinite;
    }
</style>
