import { FormBlock } from "core/form/types";
import { AirbyteJSONSchemaDefinition, AirbyteJSONSchema } from "./types";

/**
 * Returns {@link FormBlock} representation of jsonSchema
 *
 * Builds internal {@link FormBlock} from jsonSchema recursively.
 * Allows to walk through and validate schema in a more convenient way
 *
 * @param jsonSchema
 * @param key
 * @param path
 * @param parentSchema
 */
export const jsonSchemaToUiWidget = (
  jsonSchema: AirbyteJSONSchemaDefinition,
  key = "",
  path: string = key,
  parentSchema?: AirbyteJSONSchemaDefinition
): FormBlock => {
  const isRequired = isKeyRequired(key, parentSchema);

  // TODO: decide what to do with boolean case
  if (typeof jsonSchema === "boolean") {
    return {
      _type: "formItem",
      path: key,
      fieldKey: key,
      type: "null",
      isRequired,
      isSecret: false,
    };
  }

  if (jsonSchema.oneOf?.length && jsonSchema.oneOf.length > 0) {
    const conditions = Object.fromEntries(
      jsonSchema.oneOf.map((condition) => {
        if (typeof condition === "boolean") {
          return [];
        }
        return [
          condition.title,
          jsonSchemaToUiWidget(
            { ...condition, type: jsonSchema.type },
            key,
            path
          ),
        ];
      })
    );

    return {
      _type: "formCondition",
      title: jsonSchema.title,
      description: jsonSchema.description,
      path: path || key,
      fieldKey: key,
      conditions,
      isRequired,
    };
  }

  if (
    jsonSchema.type === "array" &&
    typeof jsonSchema.items === "object" &&
    !Array.isArray(jsonSchema.items) &&
    jsonSchema.items.type === "object"
  ) {
    return {
      ...pickDefaultFields(jsonSchema),
      _type: "objectArray",
      path: path || key,
      fieldKey: key,
      properties: jsonSchemaToUiWidget(jsonSchema.items, key, path),
      isRequired,
    };
  }

  if (jsonSchema.type === "object") {
    const properties = Object.entries(
      jsonSchema.properties || []
    ).map(([k, schema]) =>
      jsonSchemaToUiWidget(schema, k, path ? `${path}.${k}` : k, jsonSchema)
    );

    return {
      ...pickDefaultFields(jsonSchema),
      _type: "formGroup",
      jsonSchema,
      path: path || key,
      fieldKey: key,
      properties,
      isRequired,
    };
  }

  return {
    ...pickDefaultFields(jsonSchema),
    _type: "formItem",
    path: path || key,
    fieldKey: key,
    isRequired,
    isSecret: !!jsonSchema.airbyte_secret,
    multiline: !!jsonSchema.multiline,
    type:
      (Array.isArray(jsonSchema.type) ? jsonSchema.type[0] : jsonSchema.type) ??
      "null",
  };
};

function isKeyRequired(
  key: string,
  parentSchema?: AirbyteJSONSchemaDefinition
): boolean {
  const isRequired =
    (typeof parentSchema !== "boolean" &&
      Array.isArray(parentSchema?.required) &&
      parentSchema?.required.includes(key)) ||
    false;

  return isRequired;
}

const defaultFields: Array<keyof AirbyteJSONSchema> = [
  "default",
  "examples",
  "description",
  "pattern",
  "order",
  "const",
  "title",
];

const pickDefaultFields = (
  schema: AirbyteJSONSchema
): Partial<AirbyteJSONSchema> => {
  const partialSchema: Partial<AirbyteJSONSchema> = {
    ...Object.fromEntries(
      Object.entries(schema).filter(([k]) =>
        defaultFields.includes(k as keyof AirbyteJSONSchema)
      )
    ),
  };

  if (
    typeof schema.items === "object" &&
    !Array.isArray(schema.items) &&
    schema.items.enum
  ) {
    partialSchema.enum = schema.items.enum;
  } else if (schema.enum) {
    partialSchema.enum = schema.enum;
  }

  return partialSchema;
};