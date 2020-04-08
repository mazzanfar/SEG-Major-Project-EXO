import React, { Component, Fragment } from "react";
import { useDispatch, useSelector, useEffect } from "react-redux";
import { Dropdown, Button, Icon, Label, Item, Rating } from "semantic-ui-react";
import Comments from "./Comments";
import { ratePost } from "../../../actions/ratings";

function PostDetail(props) {
    const user = useSelector((state) => state.auth.user);
    const dispatch = useDispatch();
    const state = {
        options: [
            { key: "edit", icon: "edit", text: "Edit Post", value: "edit" },
            {
                key: "delete",
                icon: "delete",
                text: "Remove Post",
                value: "delete",
            },
            { key: "hide", icon: "hide", text: "Hide Post", value: "hide" },
        ],
    };

    /*
    handleLikePost() {
        const like = {"post": this.props.post.id, "user": 14, "vote_type": "like"}
        this.props.likePost(like)
    }
    */

    const checkRating = (e, data) => {
        const rating = {
            rating: data.rating,
            user: user.id,
            post: props.post.id,
        };
        //console.log(rating);
        dispatch(ratePost(rating));
    };

    return (
        <Fragment>
            <Item>
                <Item.Image
                    size="tiny"
                    src="https://react.semantic-ui.com/images/wireframe/image.png"
                />
                <Item.Content>
                    <Item.Header as="a">{props.post.title}</Item.Header>
                    <Item.Meta>
                        Posted by {props.post.author_username} on{" "}
                        {props.post.tidy_date}
                    </Item.Meta>
                    <Item.Description>{props.post.content}</Item.Description>
                    {props.children}
                    <Item.Extra>
                        {props.post.topic_names.map((topic) => (
                            <Label href={"/topic/" + topic.name}>
                                {topic.name}
                            </Label>
                        ))}
                    </Item.Extra>
                    <Button.Group color="teal">
                        <Button>Save</Button>
                        <Dropdown
                            className="button icon"
                            floating
                            options={state.options}
                            trigger={<React.Fragment />}
                        />
                    </Button.Group>
                    <Rating
                        maxRating={5}
                        defaultRating={props.post.rating}
                        onRate={checkRating}
                        icon="star"
                        size="tiny"
                    />
                </Item.Content>
            </Item>
            <Comments post={props.post} />
        </Fragment>
    );
}

export default PostDetail;
