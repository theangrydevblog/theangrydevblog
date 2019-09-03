WITH subs_ids AS
(
  SELECT
    subscriber_id
  FROM
    theangrydev_subscription
  WHERE
    tag_id
  IN
    (
      SELECT
        tag_id
      FROM
        theangrydev_tag_posts
      WHERE post_id={{ POST_ID }}
    )
) SELECT
  email
FROM
  subs_ids
LEFT JOIN
  theangrydev_user
ON
  theangrydev_user.id = subs_ids.subscriber_id;
