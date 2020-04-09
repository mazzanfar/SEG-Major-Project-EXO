import React, { Component, Fragment } from "react";
import { useDispatch, useSelector, useEffect } from "react-redux";
import { Dropdown, Button, Icon, Label, Item, Rating } from "semantic-ui-react";
import Comments from "./Comments";
import { ratePost, updateRating } from "../../../actions/ratings";

function PostDetail(props) {
    const user = useSelector((state) => state.auth.user);
    const getRating = () => {
        if (!user) {
            return 3;
        }
        // Filter all the ratings of this post based on logged in user's id
        const user_rating = props.post.ratings.filter(
            (rating) => rating.user === user.id
        );
        // If we found a rating, return its value else return a default of 0
        if (user_rating.length != 0) return user_rating[0].rating;
        return 0;
    };
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

    const checkRating = (e, data) => {
        const rating = {
            id: 1,
            rating: data.rating,
            user: user.id,
            content: props.post.id,
        };
        dispatch(ratePost(rating));
        dispatch(updateRating(rating));
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
                    Average rating: {props.post.avg_rating}
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
                        defaultRating={getRating()}
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
