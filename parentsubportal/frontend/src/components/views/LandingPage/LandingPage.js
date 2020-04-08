import React, { Fragment } from "react";
import BlogPosts from "./BlogPosts";
import { useDispatch } from "react-redux";
import { Button, Image, Header, Modal } from "semantic-ui-react";
import PostForm from "./PostForm";
import Test from "./TestComponent";
import { getUser } from "../../../actions/auth";

export default function LandingPage() {
    const dispatch = useDispatch();
    dispatch(getUser());
    const inlineStyle = {
        modal: {
            marginTop: "0px !important",
            marginLeft: "50",
            marginRight: "50",
            height: "auto",
            top: "auto",
            left: "auto",
            bottom: "auto",
            right: "auto",
            overflow: "initial",
        },
    };
    return (
        <Fragment>
            <Modal
                style={inlineStyle.modal}
                trigger={<Button>Add Blog Post</Button>}
            >
                <Modal.Header>Add a Blog Post</Modal.Header>
                <Modal.Content>
                    <PostForm />
                </Modal.Content>
            </Modal>
            <BlogPosts />
        </Fragment>
    );
}
