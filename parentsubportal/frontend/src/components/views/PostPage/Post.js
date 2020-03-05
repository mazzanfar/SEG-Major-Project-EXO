import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";

function Post(props) {

    return (
        <Fragment>
            <div>
                <h1>{props.match.params.postId}</h1>
            </div>
        </Fragment>
    )
}

export default Post
