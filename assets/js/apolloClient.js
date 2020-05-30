import ApolloClient from 'apollo-boost';

const djangoCookie = document.cookie.includes("csrftoken") ? document.cookie.split("csrftoken=")[1] : null
const djangoCSRF = document.querySelector("input[name='csrfmiddlewaretoken']") ? document.querySelector("input[name='csrfmiddlewaretoken']").value : null

const token = djangoCookie || djangoCSRF

const client = new ApolloClient({
  uri: "/graphql/",
  headers: {
      'X-CSRFToken': token
  }
});

export default client