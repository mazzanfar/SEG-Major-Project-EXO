import React, { Component } from "react";
import YouTube from "react-youtube";

export default class VideoDetail extends Component {
    render() {
        const opts = {
            height: "460",
            width: "640",
            playersVars: {
                autoplay: 1,
            },
        };

        return (
            <YouTube
                videoId="2g811Eo7K8U"
                opts={opts}
                onReady={this._onReady}
            />
        );
    }
}
