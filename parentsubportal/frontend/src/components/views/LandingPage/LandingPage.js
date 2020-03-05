import React, { Fragment } from "react";
import Posts  from "./Posts";
import Search  from "./search/index";
import Form  from "./Form";

export default function LandingPage() {
    return (
        <Fragment>
            <Search />
            <Posts />
            <Form />
        </Fragment>
        );
}
