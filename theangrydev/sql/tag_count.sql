WITH tag_counts AS (
  SELECT
    tag_id, COUNT(*)
  FROM
    theangrydev_tag_posts
  GROUP BY
    tag_id
) SELECT
  theangrydev_tag.id,
  theangrydev_tag.name,
  tag_counts.count
FROM
 tag_counts
LEFT JOIN
  theangrydev_tag
ON
  tag_counts.tag_id = theangrydev_tag.id;
