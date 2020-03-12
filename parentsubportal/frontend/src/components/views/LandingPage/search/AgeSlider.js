import React, { Component } from 'react';
import { Slider, Rail, Handles, Tracks, Ticks, Handles } from "react-compound-slider";

export function Handle({
    handle: {id, value, percent},
    getHandleProps
})

const sliderStyle = {  // Give the slider some width
  position: 'relative',
  width: '100%',
  height: 80,
  border: '1px solid steelblue'
}

const railStyle = {
  position: 'absolute',
  width: '100%',
  height: 10,
  marginTop: 35,
  borderRadius: 5,
  backgroundColor: '#8B9CB6',
}

export class AgeSlider extends Component {
    render() {
        return (
            <Slider
                rootStyle={sliderStyle /* inline styles for the outer div. Can also use className prop. */}
                domain={[0, 100]}
                values={[10]}
            >
                <div style={railStyle /* Add a rail as a child.  Later we'll make it interactive. */} />
            </Slider>
            )
    }
}
