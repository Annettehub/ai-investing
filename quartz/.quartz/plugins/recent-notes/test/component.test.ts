import { describe, expect, it } from "vitest";
import { RecentNotes } from "../src/index";

describe("RecentNotes", () => {
  it("is exported as a function", () => {
    expect(typeof RecentNotes).toBe("function");
  });

  it("returns a component with css property", () => {
    const component = RecentNotes();
    expect(typeof component).toBe("function");
    expect(typeof component.css).toBe("string");
  });
});
